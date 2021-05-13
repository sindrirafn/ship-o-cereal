
function updateCartButtons() {
    var updateButtons = document.getElementsByClassName("update-cart")


    for (var i = 0; i < updateButtons.length; i++) {

        updateButtons[i].addEventListener("click", function () {
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log('productID = ', productId, ' action: ', action)
            console.log('User: ', user)
            if (user === 'AnonymousUser') {
                console.log('User not logged in, not added to cart')
            } else {
                updateUserCart(productId, action)
            }
        });

}}

updateCartButtons();
// Function that sends post request to view to update the cart
function updateUserCart(productId, action){

    let url = 'update_cart/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFTOKEN':csrftoken
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })
        .then((response) => {
            console.log('response', response)
        })
}

