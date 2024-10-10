// document.getElementById('images').addEventListener('change', function(event) {
//     const file = event.target.files[0];
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             const previewImage = document.getElementById('preview-image');
//             previewImage.src = e.target.result;
//             previewImage.classList.remove('hidden');
//         };
//         reader.readAsDataURL(file);
//     }
// });document.getElementById('profileImage').src = data.profile_image
function fetchImages() {
    const parentSelect = document.getElementById('products_drops');
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

document.getElementById('imagesForm').addEventListener('submit', function (event) {
    event.preventDefault();



    // console.log('values',values);

    const formData = {
        alt: document.getElementById('alt').value,
        image: document.getElementById('image').src,
        products: document.getElementById('products_drops').value,
        is_cover: document.getElementById('is_cover').checked,
    };
    console.log("formdata: ", formData)

    fetch('http://localhost:8001/product/api/add/images/', {
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
                text: 'Image added successfully!'
            });
            document.getElementById('imagesForm').reset();
            add_ingredients_form.classList.add('hidden');
        })
        .catch(error => {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Failed to add image.'
            });
        });
});