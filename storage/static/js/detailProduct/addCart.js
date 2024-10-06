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
        alert('Please log in to add items to your cart.');
        window.location.href = 'http://localhost:8001/account/login/';
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
            console.log(data.error)

            if (data.error) {
                alert(data.error)
            }
            else{
                alert(data.message);
            }


        })

        .catch(error => console.error('Error adding to cart:', error));
}



        // console.error('Error adding to cart:', error.error));





