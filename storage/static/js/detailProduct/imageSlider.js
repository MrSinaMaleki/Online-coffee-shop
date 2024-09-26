function slideImagess() {
            const imgs = document.querySelectorAll('.img-select a');
            const imgBtns = [...imgs];
            console.log(imgBtns)
            let imgId = 1;

            imgBtns.forEach((imgItem) => {
                imgItem.addEventListener('click', (event) => {
                    event.preventDefault();
                    imgId = imgItem.dataset.id;
                    slideImage();
                });
            });

            function slideImage() {
                const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

                document.querySelector('.img-showcase').style.transform = `translateX(${-(imgId - 0) * displayWidth}px)`;
            }

        }