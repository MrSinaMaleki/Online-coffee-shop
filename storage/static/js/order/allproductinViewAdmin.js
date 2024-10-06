function productAll() {
    fetch(`http://localhost:8001/product/api/list/product`, {
        method: 'GET',
    }).then(async request => {
        let orderRows2 = ''
        const pro = await request.json()
        console.log(pro)
        for (let i in pro) {
            orderRows2 += `<tr>
                        <th></th>
                        <td>
                            <div class="flex items-center gap-3">
                                <div class="avatar">
                                    <div class="mask mask-squircle h-12 w-12">
                                        <img src="${pro[i].images.length > 0 ?
                pro[i].images[0].image :
                'https://via.placeholder.com/300'}"
                                        alt="${pro[i].title} Image" />
                                    </div>
                                </div>
                                <div>
                                    <div class="font-bold">${pro[i].title}</div>
                                    <div class="text-sm opacity-50">coming sone</div>
                                </div>
                            </div>
                        </td>
                        <td>
                            ${pro[i].category.title}
                            <br />
                            <span class="badge badge-ghost badge-sm">${pro[i].description}</span>
                        </td>
                        <td>${pro[i].timeline}</td>

                    </tr>

`;
        }
        tbody_items2.innerHTML = orderRows2
    })

}