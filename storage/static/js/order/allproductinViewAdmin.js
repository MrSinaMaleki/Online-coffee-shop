function productAll() {
    fetch(`http://localhost:8001/product/api/list/product`, {
        method: 'GET',
    }).then(async request => {
        if (!request.ok) {
            throw new Error('Network response was not ok ' + request.statusText);
        }
        let orderRows2 = '';
        const pro = await request.json();
        console.log(pro);
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
                                    <a href="http://localhost:8001/product/${pro[i].id}"><div class="font-bold">${pro[i].title}</div></a> 
                                    <div class="text-sm opacity-50">Quantity : ${pro[i].quantity}</div>   
                                </div>  
                            </div>  
                        </td>  
                        <td>  
                            ${pro[i].category.title}  
                            <br />  
                            <span class="badge badge-ghost badge-sm">${pro[i].description}</span>  
                        </td>  
                        <td>${pro[i].timeline!=null ? pro[i].timeline : "is cofffee shop"}</td>  
                    </tr>`;
        }
        tbody_items2.innerHTML = orderRows2;
    }).catch(error => {
        Swal.fire({
            title: 'Error!',
            text: 'Error fetching product list: ' + error.message,
            icon: 'error',
            confirmButtonText: 'Okay'
        });
    });
}

function category_product(id_category) {
    fetch(`http://localhost:8001/product/api/list/product/category/${id_category}`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
    }).then(async request => {
        if (!request.ok) {
            throw new Error('Network response was not ok ' + request.message); // Throw an error if the response is not ok
        }
        let orderRows2 = '';
        const pro = await request.json();
        console.log(pro);
        tbody_items2.innerHTML = "";
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
                                    <a href="http://localhost:8001/product/${pro[i].id}"><div class="font-bold">${pro[i].title}</div></a>
                                    <div class="text-sm opacity-50">Quantity : ${pro[i].quantity}</div>  
                                </div>  
                            </div>  
                        </td>  
                        <td>  
                            ${pro[i].category.title}  
                            <br />  
                            <span class="badge badge-ghost badge-sm">${pro[i].description}</span>  
                        </td>  
                         <td>${pro[i].timeline!=null ? pro[i].timeline : "is cofffee shop"}</td>  
                    </tr>`;
        }
        tbody_items2.innerHTML = orderRows2;
    }).catch(error => {
        Swal.fire({
            title: 'Error!',
            text: 'Error fetching products by category: ' + error.message,
            icon: 'error',
            confirmButtonText: 'Okay'
        });
    });
}

function FuTimeLine(timeLine) {
    fetch(`http://localhost:8001/product/api/list/restaurant/${timeLine}`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        },
    }).then(async request => {
        if (!request.ok) {
            throw new Error('Network response was not ok ' + request.statusText); // Throw an error if the response is not ok
        }
        let orderRows2 = '';
        const pro = await request.json();
        console.log(pro);
        tbody_items2.innerHTML = "";
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
                                    <a href="http://localhost:8001/product/${pro[i].id}"><div class="font-bold">${pro[i].title}</div>  </a>
                                    <div class="text-sm opacity-50">Quantity : ${pro[i].quantity}</div>  
                                </div>  
                            </div>  
                        </td>  
                        <td>  
                            ${pro[i].category.title}  
                            <br />  
                            <span class="badge badge-ghost badge-sm">${pro[i].description}</span>  
                        </td>  
                         <td>${pro[i].timeline!=null ? pro[i].timeline : "is cofffee shop"}</td>  
                    </tr>`;
        }
        tbody_items2.innerHTML = orderRows2;
    }).catch(error => {
        Swal.fire({
            title: 'Error!',
            text: 'Error fetching products by timeline: ' + error.message,
            icon: 'error',
            confirmButtonText: 'Okay'
        });
    });
}

function coffeeShop(){
        fetch(`http://localhost:8001/product/api/list/coffeeshop`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': '{{ csrf_token }}'
            }
        }).then(async request => {
        if (!request.ok) {
            throw new Error('Network response was not ok ' + request.statusText); // Throw an error if the response is not ok
        }
        let orderRows2 = '';
        const pro = await request.json();
        console.log(pro);
        tbody_items2.innerHTML = "";
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
                                    <a href="http://localhost:8001/product/${pro[i].id}"><div class="font-bold">${pro[i].title}</div>  </a>
                                    <div class="text-sm opacity-50">Quantity : ${pro[i].quantity}</div>  
                                </div>  
                            </div>  
                        </td>  
                        <td>  
                            ${pro[i].category.title}  
                            <br />  
                            <span class="badge badge-ghost badge-sm">${pro[i].description}</span>  
                        </td>  
                         <td>${pro[i].timeline!=null ? pro[i].timeline : "is cofffee shop"}</td>  
                    </tr>`;
        }
        tbody_items2.innerHTML = orderRows2;
    }).catch(error => {
        Swal.fire({
            title: 'Error!',
            text: 'Error fetching products by timeline: ' + error.message,
            icon: 'error',
            confirmButtonText: 'Okay'
        });
    });
}