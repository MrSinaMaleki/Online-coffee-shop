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
            'X-CSRFToken': '{{ csrf_token }}'
        },
    }).then(response => response.json()).then(orders => {
        console.log(orders)
        let orderRows = '';
        orders.forEach(order => {

            order.items.forEach(item => {
                console.log(item)
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
                                    <div class="text-sm opacity-50">${order.created_at}</div>
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
                            <button class="btn glass" onclick="orderAccept(${order.id})">Accept</button>
                        </th>`
        });
        tbody_items.innerHTML = orderRows;
    });
}
