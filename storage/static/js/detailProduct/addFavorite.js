        let liked_id = document.querySelector("#liked_id")

        const showAlert = (message) => {
            alert(message);
        }

        function toggleLike(element) {
            const formData=document.querySelector('#liked_id')
            let data = new FormData(formData)
            if (userAuthInputDetail === "True") {
                const isLiked = element.classList.toggle('liked')
                fetch(`http://localhost:8001/favorite/api/favorite/create`, {
                    method: 'POST',
                    body: data,
                })

            } else {
                showAlert('pleas login your account');
            }

        }
