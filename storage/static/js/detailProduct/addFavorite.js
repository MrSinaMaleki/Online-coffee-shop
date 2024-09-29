        let liked_id = document.querySelector("#liked_id")

        const showAlert = (message) => {
            alert(message);
        }

        function toggleLike(productId, element) {

            let data = new FormData()
            data.append('products', productId)
            console.log(data)
            const userAuthentication = parseInt(userAuthInput)
            console.log(userAuthentication)

            if (userAuthInput === "True") {
                const isLiked = element.classList.toggle('liked')
                fetch(`http://${requestHost}/favorite/api/favorite/create`, {
                    method: 'POST',
                    body: data,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': '{{ csrf_token }}'
                    }

                })

            } else {
                showAlert('pleas login your account');
            }

        }
