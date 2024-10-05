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

            data.items.forEach(item => {
                cartContent += `<div class="cart-item">
                    <p>Product: ${item.product.title}</p>
                    <p>Quantity: ${item.quantity}</p>
                    <p>Price: ${item.total_price}</p>
                </div>`;
            });

            cartContent +=`<div class="cart-actions">
                    <button id="pay-button" class="btn btn-success" onclick="payForOrder(${data.id})">Pay</button>
                    <button id="cancel-button" class="btn btn-danger" onclick="cancelOrder(${data.id})">Cancel</button>
                </div>`;

            document.getElementById('cart-items').innerHTML += cartContent;
        }
    })
    .catch(error => {
        console.error('Error fetching cart:', error);
        Swal.fire({
            title: 'Error',
            text: 'An error occurred while fetching the cart.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    });
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
        if (data.error) {
            Swal.fire({
                title: 'Error',
                text: data.error,
                icon: 'error',
                confirmButtonText: 'OK'
            });
        } else {
            Swal.fire({
                title: 'Payment Successful',
                text: data.message,
                icon: 'success',
                confirmButtonText: 'OK'
            }).then(() => {
                window.location.href = '/account/';
            });
        }
    })
    .catch(error => {
        console.error('Error paying for order:', error);
        Swal.fire({
            title: 'Error',
            text: 'An error occurred while processing the payment.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    });
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
        if (data.error) {
            Swal.fire({
                title: 'Error',
                text: data.error,
                icon: 'error',
                confirmButtonText: 'OK'
            });
        } else {
            Swal.fire({
                title: 'Success',
                text: 'Order canceled successfully.',
                icon: 'success',
                confirmButtonText: 'OK'
            });
            document.getElementById('cart-items').innerHTML = '<p>Order canceled successfully.</p>';
        }
    })
    .catch(error => {
        Swal.fire({
            title: 'Error',
            text: 'An error occurred while canceling the order.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    });
}
