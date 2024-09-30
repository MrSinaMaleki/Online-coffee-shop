// 'csrfmiddlewaretoken'
         const showAlert = (message) => {
            alert(message);
        }
        document.addEventListener('DOMContentLoaded', function () {
            fetch(`http://localhost:8001/product/api/list/restaurant/${time}`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
            }).then(response => response.json()).then(products => {
                const productList = document.getElementById('products-list');
                products.forEach(product => {
                    let imageSrc=""
                    let imageAlt=""
                    console.log(product.images.length)
                    if (product.images.length===0){
                        imageSrc='https://via.placeholder.com/300'
                        imageAlt="image"
                    }
                    else {
                        imageSrc=product.images[0].image
                        imageAlt=product.images[0].alt
                    }
                    console.log(product.images)
                    const productCard = `

                    <div class="card bg-base-100 w-96 shadow-xl m-2">
                        <div class="card-body">
                            <div class="like-btn ${product.favorite ? 'liked' : ''}" onclick="toggleLike(${product.id}, this)">
                                <i class="fas fa-heart"></i>
                            </div>
                            <img src="${imageSrc}" alt="${imageAlt}">  
                            <a href='http://${requestHost}/product/${product.id}'>
                            <div class="product-title">${product.title}</div>
                            <div class="product-price">$${product.price}</div>
                            <a href="#" class="btn btn-primary" onclick="addToCart(${product.id})">Add to Cart</a>
                        </div>
                    </div>
                  </a>
                `;
                    productList.innerHTML += productCard;
                });
            });
        });

        function toggleLike(productId, element) {
            if (userAuthInputList === "True") {
                element.classList.toggle('liked')
                let data = new FormData()
                data.append('products', productId)
                console.log(data)
                fetch(`http://localhost:8001/favorite/api/favorite/create`, {
                    method: 'POST',
                    body: data,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': '{{ csrf_token }}'
                    }
                })
            } else {
                showAlert('pleas login your account');
            }
        }

        function addToCart(productId) {
            console.log(`Product ${productId} added to cart`);
        }