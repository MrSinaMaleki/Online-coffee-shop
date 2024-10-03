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
                historyContent += `<div class="order">
                    <h3>Order ID: ${order.id}</h3>
                    <p>Order Date: ${order.created_at}</p>
                    <p>Status: ${order.is_paid ? 'Paid' : 'Not Paid'}</p>
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
