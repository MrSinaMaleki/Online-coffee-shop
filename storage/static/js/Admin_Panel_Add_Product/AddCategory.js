 function fetchCategories() {
            const parentSelect = document.getElementById('parent');
            fetch('http://localhost:8001/product/api/add/category/')
                .then(response => response.json())
                .then(data => {
                    parentSelect.innerHTML = '<option value="">No Parent</option>';
                    data.forEach(category => {
                        const option = document.createElement('option');
                        option.value = category.id;
                        option.textContent = category.title;
                        parentSelect.appendChild(option);
                    });
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Error',
                        text: 'Failed to fetch categories.'
                    });
                });
        }

        document.getElementById('categoryForm').addEventListener('submit', function (event) {
            event.preventDefault();

            const formData = {
                title: document.getElementById('title').value,
                parent: document.getElementById('parent').value || null
            };

            fetch('http://localhost:8001/product/api/add/category/', {
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
                    text: 'Category added successfully!'
                });
                document.getElementById('categoryForm').reset();
                add_category_form.classList.add('hidden');
            })
            .catch(error => {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Failed to add category.'
                });
            });
        });