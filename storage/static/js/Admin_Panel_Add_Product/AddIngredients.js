function fetchIngredients() {
    const parentSelect = document.getElementById('products_drop');
    fetch('http://localhost:8001/product/api/add/product/')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            parentSelect.innerHTML = '<option value="">-----</option>';
            data.forEach(product => {
                const option = document.createElement('option');
                option.value = product.id;
                option.textContent = product.title;
                parentSelect.appendChild(option);
            });
        })
        .catch(error => {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Failed to fetch products.!!!'
            });
            console.log('error:', error)
        });
}

document.getElementById('ingredientsForm').addEventListener('submit', function (event) {
    event.preventDefault();


    let options = document.getElementById('products_drop').selectedOptions;
    let values = Array.from(options).map(({value}) => value);
    // console.log('values',values);

    const formData = {
        title: document.getElementById('title_inp').value,
        products: values
    };
    console.log("formdata: ", formData)

    fetch('http://localhost:8001/product/api/add/ingredients/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfTokens
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            Swal.fire({
                icon: 'success',
                title: 'Success',
                text: 'Ingredients added successfully!'
            });
            document.getElementById('ingredientsForm').reset();
            add_ingredients_form.classList.add('hidden');
        })
        .catch(error => {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Failed to add ingredients.'
            });
        });
});