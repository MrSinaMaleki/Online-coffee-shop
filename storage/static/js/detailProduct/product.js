document.addEventListener('DOMContentLoaded', function (event) {

    const imagePreview = document.querySelector('#image_parent')
    const imageSliders = document.querySelector("#image_items")
    const ingredients_title = document.querySelector("#ingredients_title")
    const description_short = document.querySelector("#description_short")
    const price_product = document.querySelector("#price_product")
    const category = document.querySelector("#category")
    const product_title = document.querySelector("#product_title")


    fetch(`api/detail/product/${pkId}`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        },
    }).then(async (response) => {
        const productes = await response.json()

        console.log(productes)
        imagePreview.innerHTML = ""
        imageSliders.innerHTML = ""
        ingredients_title.innerHTML = ""
        description_short.innerHTML = productes.description
        price_product.innerHTML = productes.price
        category.innerHTML = productes.category.title
        product_title.innerHTML = productes.title
        if (productes.favorite) {

            liked_id.classList.toggle('liked')
        }
        console.log()
        if (productes.images.length > 1) {
            for (i in productes.ingredients) {

                let el = `
                    <li>${productes.ingredients[i].title}</li>`
                ingredients_title.innerHTML += el
            }
            for (i in productes.images) {
                const imageEl = `
                <img src="${productes.images[i].image}"
                             alt="${productes.images[i]}">`

                const imageSlider = `
                     <div class="img-item">
                        <a href="#" data-id="${i}">
                            <img src="${productes.images[i].image}"
                                 alt="${productes.images[i].alt}">
                        </a>
                    </div>
                `
                imageSliders.innerHTML += imageSlider
                imagePreview.innerHTML += imageEl
            }
        } else if (productes.images.length === 1){
            const imageEl = `
                <img src="${productes.images[0].image}"
                             alt="${productes.images[0]}">`
            imagePreview.innerHTML += imageEl
        }else {
            imagePreview.innerHTML += `<img src="https://www.k5learning.com/sites/all/files/can%27t.gif"
                             alt="image">`
        }

    }).finally(() => {
        slideImagess()
    })

})