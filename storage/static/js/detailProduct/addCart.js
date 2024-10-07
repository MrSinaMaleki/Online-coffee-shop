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

function addToCart(productId) {
    const quantity = parseInt(document.getElementById('quantity').value);

    if (userAuthInputDetail === "False") {
        Swal.fire({
            title: 'Not Logged In',
            text: 'Please log in to add items to your cart.',
            icon: 'warning',
            confirmButtonText: 'Log In',
            showCancelButton: true,
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = 'http://localhost:8001/account/login/';
            }
        });
        return;
    }

    fetch(`http://localhost:8001/order/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({
            quantity: quantity
        })
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
                text: data.message,
                icon: 'success',
                confirmButtonText: 'OK'
            });
             updateCartCount();
        }
    })
    .catch(error => {
        Swal.fire({
            title: 'Error',
            text: 'An error occurred while adding the item to the cart.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    }).finally(()=>{SafetyBuffer()});
}

function updateCartCount() {
    fetch('http://localhost:8001/order/api/numberofproduct', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        },
    })
    .then(response => response.json())
    .then(data => {
        const cartCountElement = document.getElementById('cart-count');

        if (data.item_count !== undefined) {
            cartCountElement.textContent = data.item_count;
        } else {
            cartCountElement.textContent = '0';
        }
    })
    .catch(error => console.error('Error fetching cart count:', error));


    }
