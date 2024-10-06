document.addEventListener('DOMContentLoaded', function() {
    fetchCartItems();
});


function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


function fetchCartItems() {
    fetch('http://localhost:8001/order/cart/viewcart', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById('cart-items').innerHTML = '<p>' + data.message + '</p>';
        } else {
            let cartContent = '';
            // console.log(data.id)
            // console.log(data)
            cartContent +=`<div class="cart-actions">
                    <button id="pay-button" class="btn btn-success" onclick="payForOrder(${data.id})">Pay</button>
                    <button id="cancel-button" class="btn btn-danger" onclick="cancelOrder(${data.id})">Cancel
                    </button>
                    </div>`

            data.items.forEach(item => {
                cartContent += `<div class="cart-item">
                    <p>Product: ${item.product.title}</p>
                    <p>Quantity: ${item.quantity}</p>
                    <p>Price: ${item.total_price}</p>
                </div>`;
            });
            document.getElementById('cart-items').innerHTML += cartContent;
        }
    })
    .catch(error => console.error('Error fetching cart:', error));
}

function payForOrder(orderId) {
    fetch(`http://localhost:8001/order/cart/pay/${orderId}/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            window.location.href = '/order/history_order/';
        }
    })
    .catch(error => console.error('Error paying for order:', error));
}

function cancelOrder(orderId) {
    fetch(`http://localhost:8001/order/cart/cancel/${orderId}/`, {
        method: 'POST',
       headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById('cart-items').innerHTML = '<p>Order canceled successfully.</p>';
        }
    })
    .catch(error => console.error('Error canceling order:', error));
}
