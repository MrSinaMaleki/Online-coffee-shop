function orderView() {
    button_product_detail_view.classList.add('!hidden')
    comment_accepted.classList.add('!hidden')
    orderViews.classList.remove('!hidden')

    FlagId = 0
    const tbody_items = document.querySelector('#tbody_items');
    fetch(`http://localhost:8001/order/api/ordrlist`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
    }).then(response => response.json()).then(orders => {
        console.log(orders)
        let orderRows = '';
        orders.forEach(order => {

            order.items.forEach(item => {
                const date = new Date(order.created_at);
                const formattedDate = date.toLocaleDateString();
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                const result = `${formattedDate} ${hours}:${minutes}`;
                orderRows += `<tr>
                        <th></th>
                        <td>
                            <div class="flex items-center gap-3">
                                <div class="avatar">
                                    <div class="mask mask-squircle h-12 w-12">
                                        <img src="${item.product.images.length > 0 ?
                    item.product.images[0].image :
                    'https://via.placeholder.com/300'}"
                                        alt="${item.product.title} Image" />
                                    </div>
                                </div>
                                <div>
                                    <div class="font-bold">${item.product.title}</div>
                                    <div class="text-sm opacity-50">${result}</div>
                                </div>
                            </div>
                        </td>
                        <td>
                            ${item.product.category.title}
                            <br />
                            <span class="badge badge-ghost badge-sm">${item.product.description}</span>
                        </td>
                        <td>${item.quantity}</td>

                    </tr>`;
            });
            orderRows += `  <th>
                            <button class="btn btn-success" onclick="orderAccept(${order.id})">Accept</button>
                        </th>`
        });
        tbody_items.innerHTML = orderRows;
    });
}


function orderAccept(orderid) {
    let data = new FormData();
    data.append('orderId', orderid);

    fetch(`http://localhost:8001/order/api/ordrlist`, {
        method: 'POST',
        body: data,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(errorData => {
                    Toastify({
                        text: 'Error: ' + errorData.message,
                        duration: 3000,
                        gravity: "top", // "top" or "bottom"
                        position: 'right', // "left", "center" or "right"
                        backgroundColor: "#ff0000",
                    }).showToast();
                    throw new Error('Network response was not ok');
                });
            }
            return response.json();
        })
        .then(data => {
            Toastify({
                text: 'Order accepted successfully!',
                duration: 3000,
                gravity: "top",
                position: 'right',
                backgroundColor: "#4CAF50",
            }).showToast();
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        })
        .finally(() => {
            orderView();
        });
}
