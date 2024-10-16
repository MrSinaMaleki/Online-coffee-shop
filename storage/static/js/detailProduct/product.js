

document.addEventListener('DOMContentLoaded', function (event) {

    const imagePreview = document.querySelector('#image_parent');
    const imageSliders = document.querySelector("#image_items");
    const ingredients_title = document.querySelector("#ingredients_title");
    const description_short = document.querySelector("#description_short");
    const old_price_product = document.querySelector("#old_price_product");
    const price_product = document.querySelector("#price_product");
    const category = document.querySelector("#category");
    const product_title = document.querySelector("#product_title");
    const quantityInput = document.querySelector("#quantity");
    const addToCartButton = document.querySelector(".btn");
    const score_product = document.querySelector("#score_product");
    const starRating = document.getElementById("star-rating");

    fetch(`api/detail/product/${pkId}`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        },
    }).then(async (response) => {
        console.log(response);
        if (response.status !== 200) {
            alert('no product');
        } else {
            const product = await response.json();
            console.log(product);
            imagePreview.innerHTML = "";
            imageSliders.innerHTML = "";
            ingredients_title.innerHTML = "";
            description_short.innerHTML = product.description;
            old_price_product.innerHTML = product.old_price;
            price_product.innerHTML = product.price;
            product_title.innerHTML = product.title;

            createStar(product.score, starRating);

            if (product.favorite) {
                liked_id.classList.toggle('liked');
            }
            for (i in product.ingredients) {
                let el = `
                    <li>${product.ingredients[i].title}</li>`;
                ingredients_title.innerHTML += el;
            }

            if (product.images.length > 1) {

                for (i in product.images) {
                    const imageEl = `
                <img src="${product.images[i].image}" alt="${product.images[i].alt}">`;
                    const imageSlider = `
                     <div class="img-item">
                        <a href="#" data-id="${i}">
                            <img src="${product.images[i].image}" alt="${product.images[i].alt}">
                        </a>
                    </div>`;
                    imageSliders.innerHTML += imageSlider;
                    imagePreview.innerHTML += imageEl;
                }
            } else if (product.images.length === 1) {
                const imageEl = `
                <img src="${product.images[0].image}" alt="${product.images[0].alt}">`;
                imagePreview.innerHTML += imageEl;
            } else {
                imagePreview.innerHTML += `<img src="https://via.placeholder.com/300" alt="image">`;
            }

            if (product.category.length >= 2) {
                console.log(product.category.length )
                for (i in product.category) {
                    const categorys = `  <i class="fa-solid fa-play"></i> <a href="http://localhost:8001/product/category/${product.category[i].id}" class="product-link ">${product.category[i].title}</a>`;
                    category.innerHTML += categorys;
                }
            } else {
                category.innerHTML = `<a href="http://localhost:8001/product/category/${product.category[0].id}" class="product-link ">${product.category[0].title}</a>`;
            }


            if (product.quantity === 0) {
                addToCartButton.disabled = true;
                addToCartButton.classList.add('btn-secondary');
                addToCartButton.classList.remove('btn-primary');
                addToCartButton.innerHTML = 'This product is finished';
                quantityInput.disabled = true;
            } else {
                addToCartButton.disabled = false;
                addToCartButton.classList.add('btn-primary');
                addToCartButton.classList.remove('btn-secondary');
                addToCartButton.innerHTML = 'Add to Cart <i class="fas fa-shopping-cart text-2xl"></i>';
                quantityInput.disabled = false;

            }
        }

    }).finally(() => {
        slideImagess();
        SafetyBuffer()
    });
});


function SafetyBuffer() {
    const safety_buffer = document.querySelector('#safety_buffer');
    fetch(`http://localhost:8001/product/api/product/safety/${pkId}`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        },
    })
        .then(async response => {
            // بررسی وضعیت پاسخ
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            console.log(data.quantity)

            if (data.quantity <= 3) {
                safety_buffer.innerHTML = `remaining product quantity : ${data.quantity}`;
                safety_buffer.classList.add('text-red-800');
            } else {
                safety_buffer.classList.remove('text-red-800');
            }
        })
        .catch(error => {
            // نمایش پیام خطا در صورت بروز مشکل
            alert(`Error: ${error.message}`);
        });
}

