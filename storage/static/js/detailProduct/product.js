document.addEventListener('DOMContentLoaded', function (event) {

    const imagePreview = document.querySelector('#image_parent');
    const imageSliders = document.querySelector("#image_items");
    const ingredients_title = document.querySelector("#ingredients_title");
    const description_short = document.querySelector("#description_short");
    const price_product = document.querySelector("#price_product");
    const category = document.querySelector("#category");
    const product_title = document.querySelector("#product_title");
    const quantityInput = document.querySelector("#quantity");
    const addToCartButton = document.querySelector(".btn");

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
            price_product.innerHTML = product.price;
            product_title.innerHTML = product.title;

            if (product.favorite) {
                liked_id.classList.toggle('liked');
            }

            if (product.images.length > 1) {
                for (i in product.ingredients) {
                    let el = `
                    <li>${product.ingredients[i].title}</li>`;
                    ingredients_title.innerHTML += el;
                }
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

            if (product.category.length > 1) {
                for (i in product.category) {
                    const categorys = `  <i class="fa-solid fa-play"></i> <a href="#" class="product-link ">${product.category[i].title}</a>`;
                    category.innerHTML += categorys;
                }
            } else {
                category.innerHTML = `<a href="#" class="product-link ">${product.category.title}</a>`;
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
                addToCartButton.innerHTML = 'Add to Cart';
                quantityInput.disabled = false;
            }
        }

    }).finally(() => {
        slideImagess();
        SafetyBuffer()
    });
});
