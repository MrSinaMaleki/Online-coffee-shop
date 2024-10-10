function comments_accepted() {
    FlagId = 100;
    tbody_comment.innerHTML = "";
    comment_accepted.classList.remove("!hidden");
    orderViews.classList.add("!hidden");
    button_product_detail_view.classList.add("!hidden");
    add_product_in_admin_panel_button.classList.add('!hidden');


    fetch(`http://localhost:8001/comment/comments/admin-panel`, {
        method: "GET",
    })
        .then(async (request) => {
            let comments = "";
            const pro = await request.json();
            pro.forEach((comment) => {
                const commentColorClass = 'bg-gray-100';

                comments += `  
                <tr class="${commentColorClass} mb-2">  <!-- Added margin-bottom to create space between comments -->  
                    <td>  
                        <div class="flex items-center gap-3">  
                            <div class="avatar">  
                                <div class="mask mask-squircle h-12 w-12">  
                                    <img src="${comment.user.profile_image ? comment.user.profile_image : 'https://via.placeholder.com/300'}" alt="Avatar" />  
                                </div>  
                            </div>  
                            <div>  
                                <div class="font-bold">${comment.user.email}</div>  
                                <div class="text-sm opacity-50"></div>  
                            </div>  
                        </div>  
                    </td>  
                    <td class="">  
                        <div class="p-4">  
                            <textarea class="w-full h-24 resize-none" placeholder="${comment.text}"></textarea>  
                        </div>  
                        <br />  
                        <div class="flex ">
                        <button class="btn btn-error" onclick="delete_comments(${comment.id})">delete</button>  
                        <button class="btn btn-active btn-accent mx-2 "  onclick="accept_comments(${comment.id})">accept</button>  
                        </div>
                    </td>  
                    <td>  
                        <div class="flex items-center gap-1">  
                            <div class="avatar">  
                                <div class="mask mask-squircle h-12 w-12">  
                                    <img src="${comment.product.images.length===0?  'https://via.placeholder.com/300':comment.product.images[0].image}" alt="Product" />  
                                </div>  
                            </div>  
                            <div>  
                                <div class="font-bold">${comment.product.title}</div>  
                                <div class="text-sm opacity-50">${comment.product.description}</div>  
                            </div>  
                        </div>  
                    </td>  
                <tr style="margin-bottom: 10px;"  >`;


                if (comment.reply_comments != null) {
                    const reply = comment.reply_comments;
                    const replyColorClass = 'bg-green-100';

                    comments += `  
                    <tr class="${replyColorClass} mb-2 ">  <!-- Added margin-bottom to create space between replies -->  
                        <td colspan="2">   
                            <div style="margin-left: 40px; padding: 10px;" class="flex items-center gap-2">  
                                <div class="avatar">  
                                    <div class="mask mask-squircle h-10 w-5">  
                                        <img src="${reply.user.profile_image ? reply.user.profile_image : 'https://via.placeholder.com/300'}" alt="Avatar" />  
                                    </div>  
                                </div>  
                                <div>  
                                    <div class="font-bold">${reply.user.email}</div>  
                                </div>  
                            </div>  
                        </td>  
                        <td colspan="2">  
                            <div class="p-2 ">   
                                <textarea class="w-80 h-16 resize-none" placeholder="${reply.text}"></textarea>  
                            </div>  
                        </td>  
                    <tr style="margin-bottom: 10px;" >`;
                }
            });
            tbody_comment.innerHTML += comments;
        });
}


function delete_comments(comment_id) {

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
            let data = new FormData();
            data.append('id_comment', comment_id);
            fetch(`http://localhost:8001/comment/comments/admin-panel`, {
                method: 'DELETE',
                body: data,
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
                    comments_accepted();
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'There was an error deleting the comment: ' + error.message,
                    });
                });
        }
    });
}

function accept_comments(comment_id) {

    let data = new FormData();
    data.append('id_comment', comment_id);

    fetch(`http://localhost:8001/comment/comments/admin-panel`, {
        method: 'POST',
        body: data,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfTokens
        },
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {

            comments_accepted();
        })
        .catch(error => {

            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'There was an error processing your request: ' + error.message,
            });
        });
}