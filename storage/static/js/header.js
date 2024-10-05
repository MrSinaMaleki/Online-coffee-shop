document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
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
