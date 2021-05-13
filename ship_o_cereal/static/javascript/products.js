// var list_disp =
//     `<div class="col mb-4">
//     <div class="card shadow">
//
//         <a href="/products/${d.name}">
//             <img class="card-img-top p-3 list_img" src="${d.firstImage}"
//                  alt="${d.name}">
//
//         </a>
//
// <!--        <img src="{% static 'images/'|add:product.name|add:'.jpeg' %}" class="card-img-top p-3" alt="{{ product.name }}">-->
//         <!--Card content-->
//         <div class="card-body">
//             <!--Title-->
//             <h4 class="card-title">${d.name}</h4>
//             <!--Text-->
//             <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
//                 card's content.</p>
//             <!--Price-->
//             <h5 class="card-title">${d.price} ISK</h5>
//             <!-- Provides extra visual weight and identifies the primary action in a set of buttons -->
// <!--            <button type="button" class="btn btn-light-blue btn-md">Read more</button>-->
//             <a href="/products/${d.name}" class="btn btn-primary">Info</a>
//             <a class="btn btn-primary btn-inline" onclick="console.log(${d.id})">+Cart</a>
//             <a href="#" class="btn-floating btn btn-danger"><i class="fas fa-heart"></i></a>
//         </div>
//     </div>
// </div>`;
//

// let content;
//
// $(document).ready(function () {
//     $.ajax({
//         url: '/products?searchStr=',
//         type: 'GET',
//         success: function(resp) {
//                 content = resp.data;
//                 console.log(content)
//             },
//             error: function (xhr, status, error) {
//                 console.error(error);
//             }
//         });
//     });

$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/products?searchStr=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="col mb-4">
                                <div class="card shadow">                           
                                    <a href="/products/${d.name}">
                                        <img class="card-img-top p-3 list_img" src="${d.firstImage}"
                                             alt="${d.name}">
                                    </a>
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                                            card's content.</p>
                                        <h5 class="card-title">${d.price} ISK</h5>
                                        <a href="/products/${d.name}" class="btn btn-primary">Info</a>
                                        <a class="btn btn-primary btn-inline" onclick="console.log(${d.id})">+Cart</a>
                                        <a href="#" class="btn-floating btn btn-danger"><i class="fas fa-heart"></i></a>
                                    </div>
                                </div>
                            </div>`
                });
                $('.products').html(newHtml.join(''));
                $('#search-box').val('');
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
                    return `<div class="col mb-4">
                                <div class="card shadow">                           
                                    <a href="/products/${d.name}">
                                        <img class="card-img-top p-3 list_img" src="${d.firstImage}"
                                             alt="${d.name}">
                                    </a>
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                                            card's content.</p>
                                        <h5 class="card-title">${d.price} ISK</h5>
                                        <a href="/products/${d.name}" class="btn btn-primary">Info</a>
                                        <a class="btn btn-primary btn-inline" onclick="console.log(${d.id})">+Cart</a>
                                        <a href="#" class="btn-floating btn btn-danger"><i class="fas fa-heart"></i></a>
                                    </div>
                                </div>
                            </div>`
                });
                $('.products').html(newHtml.join(''));
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
                    return `<div class="col mb-4">
                                <div class="card shadow">                           
                                    <a href="/products/${d.name}">
                                        <img class="card-img-top p-3 list_img" src="${d.firstImage}"
                                             alt="${d.name}">
                                    </a>
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                                            card's content.</p>
                                        <h5 class="card-title">${d.price} ISK</h5>
                                        <a href="/products/${d.name}" class="btn btn-primary">Info</a>
                                        <a class="btn btn-primary btn-inline" onclick="console.log(${d.id})">+Cart</a>
                                        <a href="#" class="btn-floating btn btn-danger"><i class="fas fa-heart"></i></a>
                                    </div>
                                </div>
                            </div>`
                });
                $('.products').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })

    });

});


$(document).ready(function() {
        $("input:radio[name=cat-btn]").change(function(e) {
            $("input:radio[id=brand-filter-all]").select();
            e.preventDefault();
            var category = $(this).val();
        $.ajax({
            url: '/products?category-filter=' + category,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="col mb-4">
                                <div class="card shadow">                           
                                    <a href="/products/${d.name}">
                                        <img class="card-img-top p-3 list_img" src="${d.firstImage}"
                                             alt="${d.name}">
                                    </a>
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                                            card's content.</p>
                                        <h5 class="card-title">${d.price} ISK</h5>
                                        <a href="/products/${d.name}" class="btn btn-primary">Info</a>
                                        <a class="btn btn-primary btn-inline" onclick="console.log(${d.id})">+Cart</a>
                                        <a href="#" class="btn-floating btn btn-danger"><i class="fas fa-heart"></i></a>
                                    </div>
                                </div>
                            </div>`
                });
                $('.products').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })

    });

});