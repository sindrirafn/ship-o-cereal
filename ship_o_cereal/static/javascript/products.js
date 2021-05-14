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
                    <a href="#" class="btn-floating btn btn-danger"><i class="fas fa-heart"></i></a>
                </div>
            </div>
        </div>`
        }

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
                    $('#search-box').val('');
                    updateCartButtons();
                },
                error: function (xhr, status, error) {
                    console.error(error);
                }
            })
        });

}}

// Search function
$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
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
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })


    });
});



var input = document.getElementById("search-box");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keypress", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("search-btn").click();
  }
});



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




input.addEventListener("click", function(event) {
    $('#collapseExample').collapse('show');
    $.ajax({
            url: '/products?category-filter=' + 'Merch',
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<button class="border-0 bg-white history-item" id="search-history-item" value="${d.name}">
                                ${d.name}
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



input.addEventListener("focusout", function(event) {
    $('#collapseExample').collapse('hide');

    });

input.addEventListener("keydown", function(event) {
    $('#collapseExample').collapse('hide');

    });

// function updateUserHistory(search_string) {
//     $.ajax({
//         url: '/products?searchStr=' + searchText,
//         type: 'POST',
//         data: {
//
//         }
//
//                 success: function(resp) {
//                     var newHtml = resp.data.map(d => {
//                         return list_disp(d)
//                     });
//                     $('.products').html(newHtml.join(''));
//                     $('#search-box').val('');
//                     updateCartButtons();
//                 },
//                 error: function (xhr, status, error) {
//                     console.error(error);
//                 }
//             })
//
//     fetch(url, {
//         method: 'POST',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFTOKEN':csrftoken
//         },
//         body:JSON.stringify({'productId': productId, 'action':action})
//     })
//         .then((response) => {
//             console.log('response', response)
//         })
// }