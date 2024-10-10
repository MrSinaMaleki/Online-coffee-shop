function addProductButtonView() {
    add_product_in_admin_panel_button.classList.remove('!hidden')
    button_product_detail_view.classList.add('!hidden')
    orderViews.classList.add('!hidden')
    comment_accepted.classList.add('!hidden')
    FlagId = 100
}


function delete_product(id_product) {

    Swal.fire({
        title: 'Are you sure?',
        text: "This comment will be deleted!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'No, cancel!'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(`http://localhost:8001/product/api/add/product/${id_product}/`, {
                method: 'DELETE',

                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfTokens
                },
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok: ' + response.statusText);
                    }
                    return response.json();
                })
                .then(data => {
                    productAll();
                })
                .catch(error => {
                    console.log(error)
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'There was an error deleting the comment: ' + error.message,
                    });
                });
        }
    });
}

function update_product() {
}