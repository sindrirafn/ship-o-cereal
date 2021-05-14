
// Template for html form to display product list
function list_disp(x) {
    return `<div class="col mb-4">
            <div class="card shadow">     
                <a href="/products/${x.name}">
                    <img class="card-img-top p-3 list_img" src="${x.firstImage}"
                         alt="${x.name}">   
                </a>
                <div class="card-body">
                    <h4 class="card-title">${x.name}</h4>
                    <p class="card-text">${x.description}</p>
                    <!--Price-->
                    <h5 class="card-title">${x.price} ISK</h5>
                    <a href="/products/${x.name}" class="btn btn-primary">Info</a>
                    <a data-product="${x.id}" data-action="add" class="btn btn-primary btn-inline update-cart" >+Cart</a>
                </div>
            </div>
        </div>`
        }

        // Performs a search within the product catalogue
function search(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/products?searchStr=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return list_disp(d)
                });
                $('.products').html(newHtml.join(''));
                $('#search-box').val('');
                updateCartButtons();
                updateSearchHistory(searchText);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })


    }

    // Identifies items displayed in search history and applies necessary functions
function searchHistoryItems() {
    var historyItems = document.getElementsByClassName("history-item")


    for (var i = 0; i < historyItems.length; i++) {

        historyItems[i].addEventListener("click", function (e) {
            e.preventDefault();
            var searchText = $(this).val();
            $.ajax({
                url: '/products?searchStr=' + searchText,
                type: 'GET',
                success: function(resp) {
                    var newHtml = resp.data.map(d => {
                        return list_disp(d)
                    });
                    $('.products').html(newHtml.join(''));
                    // $('#search-box').val('');
                    updateCartButtons();
                },
                error: function (xhr, status, error) {
                    console.error(error);
                }
            })
        });

}}

// Performs a search when 'Search' button is clicked
$(document).ready(function() {
    $('#search-btn').on('click', function (event){
        search(event)
        }
    );
});


// Below are functions for filtering
$(document).ready(function() {
        $("input:radio[name=order-by]").click(function(e) {
            e.preventDefault();
            var sorter = $(this).val();
        $.ajax({
            url: '/products?orderBy=' + sorter,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return list_disp(d)
                });
                $('.products').html(newHtml.join(''));
                updateCartButtons();
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })

    });

});

$(document).ready(function() {
        $("input:radio[name=brand-filter]").change(function(e) {
            e.preventDefault();
            var brandName = $(this).val();
        $.ajax({
            url: '/products?brand-filter=' + brandName,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return list_disp(d)
                });
                $('.products').html(newHtml.join(''));
                updateCartButtons();
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })

    });

});

$(document).ready(function() {
        $("input:radio[name=cat-btn]").change(function(e) {
            e.preventDefault();
            var category = $(this).val();
        $.ajax({
            url: '/products?category-filter=' + category,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return list_disp(d)
                });
                $('.products').html(newHtml.join(''));
                updateCartButtons();
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })

    });

});


//Posts the search string used, to be added into user search history
function updateSearchHistory(search_string) {

    let url = '/users/add_hist'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFTOKEN':csrftoken
        },
        body:JSON.stringify({'search_string': search_string})
    })
        .then((response) => {
            console.log('response', response)
        })

}

// Applies all functionality for the search bar
function formatSearchBar(){
    //Check if search bar is within document
    if (document.getElementById("search-box") !== null) {
        let input = document.getElementById("search-box")

        // functions for collapsing search-history once user exits search box or inputs letters
        input.addEventListener("focusout", function(event) {
            setTimeout(function() {

            $('#collapseExample').collapse('hide');
            }, 500);
            });

        input.addEventListener("keydown", function(event) {
            $('#collapseExample').collapse('hide');

            });

        // Shows search history when user enters the search bar
        input.addEventListener("click", function(event) {
            $('#collapseExample').collapse('show');
            $.ajax({
                    url: '/users/get_hist',
                    type: 'GET',
                    success: function(resp) {
                        var newHtml = resp.data.map(d => {
                            return `<button class="border-0 bg-white history-item" id="search-history-item" value="${d.searchItem}">
                                        ${d.searchItem}
                                    </button><br>`
                        });
                        $('.search-history').html(newHtml.join(''));
                        searchHistoryItems();
                    },
                    error: function (xhr, status, error) {
                        console.error(error);
                    }
                })
            });

        // Performs search when user hits enter within the search bar
        input.addEventListener("keypress", function (event) {
            // Number 13 is the "Enter" key on the keyboard
            if (event.keyCode === 13) {
                search(event)
            }
});
}
}

formatSearchBar()