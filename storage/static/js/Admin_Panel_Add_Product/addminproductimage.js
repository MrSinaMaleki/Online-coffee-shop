// document.getElementById('images').addEventListener('change', function(event) {
//     const files = event.target.files;
//
//
//     if (files.length > 0) {
//         const file = files[0];
//
//
//         if (file.type.startsWith('image/')) {
//             const reader = new FileReader();
//
//             reader.onload = function(e) {
//                 const previewImage = document.getElementById('preview-image');
//
//
//                 if (previewImage) {
//                     previewImage.src = e.target.result;
//                     previewImage.classList.remove('hidden');
//                 }
//             };
//
//
//             reader.readAsDataURL(file);
//         } else {
//             console.error("is not picture");
//         }
//     } else {
//         console.error("no picture chosen");
//     }
// });

function fetchImages() {
    const parentSelect = document.getElementById('products_drops');
    fetch('http://localhost:8001/product/api/add/product/')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            parentSelect.innerHTML = '';
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

    let formData = new FormData();
    const fileInput = document.getElementById('image');
    const file = fileInput.files[0];

    console.log(file)

    if (!file) {
        Swal.fire({
            icon: 'warning',
            title: 'Warning',
            text: 'Please select an image to upload.'
        });
        return;
    }

    formData.append('alt', document.getElementById('alt').value);
    formData.append('image', file); // Attach the image file directly to FormData
    formData.append('product', document.getElementById('products_drops').value);
    formData.append('is_cover', document.getElementById('is_cover').checked);
    console.log(formData)

    fetch('http://localhost:8001/product/api/add/images/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfTokens // CSRF token for security
        },
        body: formData
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            Swal.fire({
                icon: 'success',
                title: 'Success',
                text: 'Image added successfully!'
            });
            document.getElementById('imagesForm').reset();
        })
        .catch(error => {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Failed to add image. Please check your input and try again.'
            });
            console.error('Error:', error);
        });
});
