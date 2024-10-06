// function comments_accepted() {
//     FlagId = 100
//     tbody_comment.innerHTML=""
//     comment_accepted.classList.remove('!hidden')
//     orderViews.classList.add('!hidden')
//     button_product_detail_view.classList.add('!hidden')
//     fetch(`http://localhost:8001/comment/comments/admin-panel`, {
//         method: 'GET',
//     }).then(async request => {
//         let comments = ''
//         const pro = await request.json()
//         pro.forEach(comment => {
//             console.log(comment)
//             comments = `     <tr class="my-5">
//
//         <td>
//           <div class="flex items-center gap-3">
//             <div class="avatar">
//               <div class="mask mask-squircle h-12 w-12">
//                 <img
//                   src="${comment.user.profile_image ?
//                 comment.user.profile_image :
//                 'https://via.placeholder.com/300'}"
//                   alt="Avatar Tailwind CSS Component" />
//               </div>
//             </div>
//             <div>
//               <div class="font-bold">${comment.user.email}</div>
//               <div class="text-sm opacity-50"></div>
//             </div>
//           </div>
//         </td>
//         <td></td>
//         <td class="">
//             <div class="p-4">
//                  <textarea class="w-full h-24 resize-none" placeholder=${comment.text}></textarea>
//                 </div>
//
//             <br />
//
//             <button class="btn btn-error"" onclick="delete_comments(${comment.id})">delete</button>
//             <button class="btn btn-success" onclick="accept_comments(${comment.id})">accept</button>
//             </td>
//             <td></td>
//         <td>
//            <div class="flex items-center gap-3">
//                <div class="avatar">
//                     <div class="mask mask-squircle h-12 w-12">
//                  <img
//                   src="${comment.product.images ?
//                 comment.product.images[0].image :
//                 'https://via.placeholder.com/300'}"
//                   alt="Avatar Tailwind CSS Component" />
//                     </div>
//                 </div>
//                     <div>
//                      <div class="font-bold">${comment.product.title}</div>
//                 <div class="text-sm opacity-50">${comment.product.description}</div>
//             </div>
//           </div>
//         </td>
//       </tr> `
//             tbody_comment.innerHTML += comments
//         })
//
//
//     })
//
//
// }


// function comments_accepted() {
//     FlagId = 100
//     tbody_comment.innerHTML=""
//     comment_accepted.classList.remove('!hidden')
//     orderViews.classList.add('!hidden')
//     button_product_detail_view.classList.add('!hidden')
//     fetch(`http://localhost:8001/comment/comments/admin-panel`, {
//         method: 'GET',
//     }).then(async request => {
//         let comments = ''
//         const pro = await request.json()
//         pro.forEach(comment => {
//             console.log(comment)
//             // ایجاد بخش نظر اصلی
//             comments += `
//             <tr class="my-5">
//                 <td>
//                     <div class="flex items-center gap-3">
//                         <div class="avatar">
//                             <div class="mask mask-squircle h-12 w-12">
//                                 <img
//                                     src="${comment.user.profile_image ? comment.user.profile_image : 'https://via.placeholder.com/300'}"
//                                     alt="Avatar Tailwind CSS Component" />
//                             </div>
//                         </div>
//                         <div>
//                             <div class="font-bold">${comment.user.email}</div>
//                             <div class="text-sm opacity-50"></div>
//                         </div>
//                     </div>
//                 </td>
//                 <td></td>
//                 <td class="">
//                     <div class="p-4">
//                         <textarea class="w-full h-24 resize-none" placeholder="${comment.text}"></textarea>
//                     </div>
//                     <br />
//                     <button class="btn btn-error" onclick="delete_comments(${comment.id})">delete</button>
//                     <button class="btn btn-success" onclick="accept_comments(${comment.id})">accept</button>
//                 </td>
//                 <td></td>
//                 <td>
//                     <div class="flex items-center gap-3">
//                         <div class="avatar">
//                             <div class="mask mask-squircle h-12 w-12">
//                                 <img
//                                     src="${comment.product.images ? comment.product.images[0].image : 'https://via.placeholder.com/300'}"
//                                     alt="Avatar Tailwind CSS Component" />
//                             </div>
//                         </div>
//                         <div>
//                             <div class="font-bold">${comment.product.title}</div>
//                             <div class="text-sm opacity-50">${comment.product.description}</div>
//                         </div>
//                     </div>
//                 </td>
//             </tr>`;
//
//             // بررسی نظرات پاسخ (reply) و اضافه کردن آن‌ها
//             if (comment.reply_comments != null) {
//                 console.log('reply comments')
//                     comments += `
//                     <tr class="my-2">
//                         <td colspan="5">
//                             <div style="margin-left: 40px;" class="flex items-center gap-3">
//                                 <div class="avatar">
//                                     <div class="mask mask-squircle h-10 w-10">
//                                         <img
//                                             src="${comment.reply_comments.user.profile_image ? comment.reply_comments.user.profile_image : 'https://via.placeholder.com/300'}"
//                                             alt="Avatar Tailwind CSS Component" />
//                                     </div>
//                                 </div>
//                                 <div>
//                                     <div class="font-bold">${comment.reply_comments.user.email}</div>
//                                     <div class="text-sm"></div>
//                                 </div>
//                             </div>
//                         </td>
//                         <td class="">
//                     <div class="p-4">
//                         <textarea class="w-full h-24 resize-none" placeholder="${comment.reply_comments.text}"></textarea>
//                     </div>
//                     </td>
//                     </tr>`;
//
//             }
//         });
//         tbody_comment.innerHTML += comments;
//     });
// }


// function comments_accepted() {
//     FlagId = 100;
//     tbody_comment.innerHTML = "";
//     comment_accepted.classList.remove("!hidden");
//     orderViews.classList.add("!hidden");
//     button_product_detail_view.classList.add("!hidden");
//
//     fetch(`http://localhost:8001/comment/comments/admin-panel`, {
//         method: "GET",
//     })
//         .then(async (request) => {
//             let comments = "";
//             const pro = await request.json();
//             pro.forEach((comment) => {
//                 // رنگ برای نظر اصلی
//                 const commentColorClass = 'bg-gray-100'; // می‌توانید رنگ را تغییر دهید
//
//                 comments += `
//                 <tr class="${commentColorClass}">
//                     <td>
//                         <div class="flex items-center gap-3">
//                             <div class="avatar">
//                                 <div class="mask mask-squircle h-12 w-12">
//                                     <img
//                                         src="${comment.user.profile_image ? comment.user.profile_image : 'https://via.placeholder.com/300'}"
//                                         alt="Avatar Tailwind CSS Component" />
//                                 </div>
//                             </div>
//                             <div>
//                                 <div class="font-bold">${comment.user.email}</div>
//                                 <div class="text-sm opacity-50"></div>
//                             </div>
//                         </div>
//                     </td>
//                     <td class="">
//                         <div class="p-4">
//                             <textarea class="w-full h-24 resize-none" placeholder="${comment.text}"></textarea>
//                         </div>
//                         <br />
//                         <button class="btn btn-error" onclick="delete_comments(${comment.id})">delete</button>
//                         <button class="btn btn-success" onclick="accept_comments(${comment.id})">accept</button>
//                     </td>
//                     <td>
//                         <div class="flex items-center gap-3">
//                             <div class="avatar">
//                                 <div class="mask mask-squircle h-12 w-12">
//                                     <img
//                                         src="${comment.product.images ? comment.product.images[0].image : 'https://via.placeholder.com/300'}"
//                                         alt="Avatar Tailwind CSS Component" />
//                                 </div>
//                             </div>
//                             <div>
//                                 <div class="font-bold">${comment.product.title}</div>
//                                 <div class="text-sm opacity-50">${comment.product.description}</div>
//                             </div>
//                         </div>
//                     </td>
//                 </tr>`;
//
//                 // بررسی و اضافه کردن پاسخ
//                 if ( comment.reply_comments!=null) {
//                     const reply = comment.reply_comments; // فرض میکنیم تنها یک پاسخ وجود دارد
//                     const replyColorClass = 'bg-green-100'; // می‌توانید رنگ پاسخ را تغییر دهید
//
//                     comments += `
//                     <tr class="${replyColorClass}">
//                         <td colspan="5">
//                             <div style="margin-left: 40px;" class="flex items-center gap-3">
//                                 <div class="avatar">
//                                     <div class="mask mask-squircle h-10 w-10">
//                                         <img
//                                             src="${reply.user.profile_image ? reply.user.profile_image : 'https://via.placeholder.com/300'}"
//                                             alt="Avatar Tailwind CSS Component" />
//                                     </div>
//                                 </div>
//                                 <div>
//                                     <div class="font-bold">${reply.user.email}</div>
//
//                                 </div>
//                             </div>
//                         </td>
//                         <td class="">
//                             <div class="p-4">
//                                 <textarea class="w-full h-24 resize-none" placeholder="${reply.text}"></textarea>
//                             </div>
//                         </td>
//                         <td><div class="font-bold">${reply.user.email}</div> </td>
//                         <td><div class="font-bold">${reply.user.email}</div> </td>
//                     </tr>`;
//                 }
//             });
//             tbody_comment.innerHTML += comments;
//         });
// }


function comments_accepted() {
    FlagId = 100;
    tbody_comment.innerHTML = "";
    comment_accepted.classList.remove("!hidden");
    orderViews.classList.add("!hidden");
    button_product_detail_view.classList.add("!hidden");

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
                        <button class="btn btn-error" onclick="delete_comments(${comment.id})">delete</button>  
                        <button class="btn btn-success" onclick="accept_comments(${comment.id})">accept</button>  
                    </td>  
                    <td>  
                        <div class="flex items-center gap-1">  
                            <div class="avatar">  
                                <div class="mask mask-squircle h-12 w-12">  
                                    <img src="${comment.product.images ? comment.product.images[0].image : 'https://via.placeholder.com/300'}" alt="Product" />  
                                </div>  
                            </div>  
                            <div>  
                                <div class="font-bold">${comment.product.title}</div>  
                                <div class="text-sm opacity-50">${comment.product.description}</div>  
                            </div>  
                        </div>  
                    </td>  
                <tr style="margin-bottom: 10px;"  >`;

                // بررسی و اضافه کردن پاسخ
                if (comment.reply_comments != null) {
                    const reply = comment.reply_comments; // فرض بر این است که تنها یک پاسخ وجود دارد
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