       let userAuthInput = '{{ request.user.is_authenticated }}'
         const showAlert = (message) => {
            alert(message);
        }
        document.addEventListener('DOMContentLoaded', function () {
            fetch('/product/api/list/product', {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
            }).then(response => response.json()).then(products => {
                const productList = document.getElementById('products-list');
                products.forEach(product => {

                    console.log(product.images)
                    const productCard = `

                    <div class="card bg-base-100 w-96 shadow-xl m-2">
                        <div class="card-body">
                            <div class="like-btn ${product.favorite ? 'liked' : ''}" onclick="toggleLike(${product.id}, this)">
                                <i class="fas fa-heart"></i>
                            </div>
                            <img src="${product.images[0].image}" alt="${product.images[0].alt}">
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
            if (userAuthInput === "True") {
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