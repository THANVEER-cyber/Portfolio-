const cart = [];
const cartList = document.getElementById('cart-list');
const totalPrice = document.getElementById('total-price');

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', event => {
        const product = event.target.closest('.product');
        const productName = product.getAttribute('data-name');
        const productPrice = parseFloat(product.getAttribute('data-price'));

        // Add product to cart array
        cart.push({ name: productName, price: productPrice });

        // Update cart UI
        updateCart();
    });
});

function updateCart() {
    cartList.innerHTML = '';
    let total = 0;

    cart.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = '${item.name} - $${item.price}';
        cartList.appendChild(listItem);
        total += item.price;
    });

    totalPrice.textContent = total.toFixed(2);
}