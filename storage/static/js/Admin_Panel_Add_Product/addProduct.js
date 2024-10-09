function addProducts() {

    fetch('http://localhost:8001/product/api/add/category/')
        .then(response => response.json())
        .then(data => {
            const categorySelect = document.getElementById("category");
            data.forEach(category => {
                let option = document.createElement("option");
                option.value = category.id;
                option.text = category.title;
                console.log(option)
                categorySelect.appendChild(option);
            });
        })
        .catch(error => console.error("Error fetching categories:", error));


    // Handle form submission
    document.getElementById("productForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        const formData = {
            title: document.getElementById("title_addProduct").value,
            off: document.getElementById("off").value,
            old_price: document.getElementById("old_price").value,
            quantity: document.getElementById("quantity").value,
            serial_number: document.getElementById("serial_number").value,
            description: document.getElementById("description").value,
            is_coffee_shop: document.getElementById("is_coffee_shop").checked,
            timeline: document.getElementById("timeline").value,
            category: document.getElementById("category").value
        };



        console.log(formData)

        fetch('http://localhost:8001/product/api/add/product/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfTokens,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),

        })
            .then(response => response.json())
            .then(data => {
                console.log("Product added successfully:", data);
                Swal.fire({
                    title: 'Successful!',
                    text: 'Added the product Successfully',
                    icon: 'success',
                    confirmButtonText: 'Cool ;)',
                    willClose: () => {
                        window.location.replace("http://localhost:8001/order/admin/")
                    }
                })


            })
            .catch(error => {

                console.error("Error adding product:", error);
                alert("There was an error adding the product.");
            });
    });
}