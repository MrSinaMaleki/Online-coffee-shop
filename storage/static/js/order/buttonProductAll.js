    function productDetail() {
        button_product_detail_view.classList.remove('!hidden')
        orderViews.classList.add('!hidden')
        comment_accepted.classList.add('!hidden')
        FlagId = 100
        fetch(`http://localhost:8001/product/api/list/category`, {
            method: 'GET',
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
                let el = ''
                data.forEach(category => {
                    el += `<button class="btn btn-outline mx-3 btn-secondary" onclick="category_product(${category.id})">${category.title}</button>`
                })
                category_menu.innerHTML = el

            })
            .catch(error => {
                console.error('There has been a problem with your fetch operation:', error);
            }).finally(() => {
            productAll()
        })

    }