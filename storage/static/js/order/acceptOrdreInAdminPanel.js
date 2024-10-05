  function orderAccept(orderid) {


        let data = new FormData();
        data.append('orderId', orderid);

        fetch(`http://localhost:8001/order/api/ordrlist`, {
            method: 'POST',
            body: data,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie(csrftoken)
            },
        })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(errorData => {
                        alert('Error: ' + errorData.message);
                        throw new Error('Network response was not ok');
                    });
                }
                return response.json();
            })
            .then(data => {
                alert('Order accepted successfully!');

            })
            .catch(error => {
                console.error('There has been a problem with your fetch operation:', error);
            }).finally(() => {
            orderView()
        })

    }