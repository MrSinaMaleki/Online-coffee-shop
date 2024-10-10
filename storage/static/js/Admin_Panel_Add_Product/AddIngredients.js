 function fetchIngredients() {
            const parentSelect = document.getElementById('product');
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
                        text: 'Failed to fetch products.'
                    });
                });
        }

        document.getElementById('ingredientsForm').addEventListener('submit', function (event) {
            event.preventDefault();

            const formData = {
                title: document.getElementById('title').value,
                products: document.getElementById('product').value || null
            };

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