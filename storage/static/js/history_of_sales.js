document.addEventListener('DOMContentLoaded', function() {
    fetchOrderHistory();
});

function fetchOrderHistory() {
    fetch('/order/history/', {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById('order-history').innerHTML = '<p>' + data.message + '</p>';
        } else {
            let historyContent = '';
            data.forEach(order => {

                const date = new Date(order.created_at);
                const formattedDate = date.toLocaleDateString();
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                const result = `${formattedDate} ${hours}:${minutes}`;

                const date2 = new Date(order.updated_at);
                const formattedDate2 = date2.toLocaleDateString();
                const hours2 = date2.getHours().toString().padStart(2, '0');
                const minutes2 = date2.getMinutes().toString().padStart(2, '0');
                const result2 = `${formattedDate2} ${hours2}:${minutes2}`;


                historyContent += `<div class="order">
                    <h3>Order ID: ${order.id}</h3>
                    <p>Order Date: ${result}</p> 
                    <p>Order Update: ${result2}</p>
                    <p>Status: ${order.is_paid ? 'Paid 💵' : 'Not Paid'} - ${order.is_completed ? 'Completed ✅' : 'Not Completed ❎'}</p>
                    <div class="order-items">
                        ${order.items.map(item => `
                            <div class="order-item">
                                <p>Product: ${item.product.title}</p>
                                <p>Quantity: ${item.quantity}</p>
                                <p>Price: ${item.total_price}</p>
                            </div>
                        `).join('')}
                    </div>
                    <hr>
                </div>`;
            });
            document.getElementById('order-history').innerHTML = historyContent;
        }
    })
    .catch(error => console.error('Error fetching order history:', error));
}
