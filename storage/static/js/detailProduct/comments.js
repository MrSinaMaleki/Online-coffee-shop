
    const commentSection = document.getElementById('commentSection');
    const commentForm = document.getElementById('commentForm');
    const newCommentForm = document.getElementById('newCommentForm');

    // Just Making stars
    function createStarRating(score) {
        const starsDiv = document.createElement('div');
        starsDiv.className = 'text-yellow-500';
        for (let i = 0; i < score; i++) {
            const star = document.createElement('span');
            star.innerHTML = '★';
            starsDiv.appendChild(star);
        }
        return starsDiv;
    }

        function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Recursive function to display comments and replays
    function displayComment(comment) {
        const commentDiv = document.createElement('div');
        commentDiv.className = 'mb-4 p-4 bg-white rounded-lg shadow-sm';
        commentDiv.setAttribute('data-comment-id', comment.id);

        const userDiv = document.createElement('div');
        userDiv.className = 'flex items-start mb-2';


        const profileImageBox = document.createElement('div');
        profileImageBox.className = 'profile-image-box mr-2';

        const profileImage = document.createElement('img');
        profileImage.src = comment.user.profile_image || 'https://via.placeholder.com/150'
        profileImage.alt = comment.user.username;

        profileImageBox.appendChild(profileImage);
        userDiv.appendChild(profileImageBox);

        const username = document.createElement('span');
        username.className = 'font-semibold text-gray-800';
        username.textContent = comment.user.username;


        const scoreDiv = createStarRating(comment.score);
        scoreDiv.className = 'ml-2';

        userDiv.appendChild(username);
        userDiv.appendChild(scoreDiv);
        commentDiv.appendChild(userDiv);


        const textDiv = document.createElement('div');
        textDiv.className = 'text-gray-800 mt-1';
        textDiv.textContent = comment.text;

        commentDiv.appendChild(textDiv);


        const replyButton = document.createElement('button');
        replyButton.className = 'mt-2 px-2 py-1 bg-indigo-500 text-white rounded hover:bg-indigo-600';
        replyButton.textContent = 'Reply';
        replyButton.onclick = (event) => {
            event.stopPropagation();
            showReplyForm(commentDiv, comment.id);
        };
        commentDiv.appendChild(replyButton);


        if (comment.reply_comments && comment.reply_comments.length > 0) {
            const repliesDiv = document.createElement('div');
            repliesDiv.className = 'ml-4 mt-2 border-l-2 border-gray-300 pl-2';

            comment.reply_comments.forEach(reply => {
                repliesDiv.appendChild(displayComment(reply));
            });

            commentDiv.appendChild(repliesDiv);
        }

        return commentDiv;
    }


    // document.getElementById('addCommentButton').addEventListener('click', () => {
    //
    // });

    function formToggler() {
        commentForm.classList.toggle('hidden');
    }


    newCommentForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const commentText = document.getElementById('commentText').value;
        const commentScore = document.getElementById('commentScore').value;


        fetch('http://localhost:8001/comment/add_comment/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                text: commentText,
                score: commentScore,
                user: userId,
                product: productId
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(() => {

            location.reload();
        })
        .catch(error => {
            console.error('Error adding comment:', error);
        });
    });


    function showReplyForm(commentDiv, commentId) {


        const existingReplyForm = commentDiv.querySelector('.replyForm');
        if (existingReplyForm) {
            existingReplyForm.remove();
        }

        const replyFormDiv = document.createElement('div');
        replyFormDiv.className = 'mt-2 p-2 bg-gray-50 border rounded-lg replyForm';

        const replyForm = document.createElement('form');
        replyForm.onsubmit = (event) => handleReplySubmit(event, commentId);

        const replyText = document.createElement('textarea');
        replyText.placeholder = 'Reply...';
        replyText.className = 'block w-full border border-gray-300 rounded-md mt-1';
        replyText.required = true;

        const replyScore = document.createElement('input');
        replyScore.type = 'number';
        replyScore.min = 1;
        replyScore.max = 5;
        replyScore.placeholder = 'Score (1-5)';
        replyScore.className = 'block w-full border border-gray-300 rounded-md mt-1';
        replyScore.required = true;

        replyForm.appendChild(replyText);
        replyForm.appendChild(replyScore);
        replyForm.appendChild(document.createElement('br'));
        const submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.className = 'mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600';
        submitButton.textContent = 'Submit Reply';
        replyForm.appendChild(submitButton);

        replyFormDiv.appendChild(replyForm);
        commentDiv.appendChild(replyFormDiv);
    }

    // Handle reply submission
    function handleReplySubmit(event, commentId) {
        event.preventDefault();

        const replyText = event.target.querySelector('textarea').value;
        const replyScore = event.target.querySelector('input[type="number"]').value;


        fetch(`http://localhost:8001/comment/adding_reply/${commentId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                text: replyText,
                score: replyScore,
                user: userId,
                product: productId,
                reply_to: commentId
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(() => {

            location.reload();
        })
        .catch(error => {
            console.error('Error adding reply:', error);
        });
    }


    function fetchComments() {
        fetch(`http://localhost:8001/comment/comments/detail/${productId}`)
            .then(response => response.json())
            .then(comments => {
                comments.forEach(comment => {
                    const commentDiv = displayComment(comment);
                    commentSection.appendChild(commentDiv);
                });
            })
            .catch(error => {
                console.error('Error fetching comments:', error);
            });
    }


    fetchComments();