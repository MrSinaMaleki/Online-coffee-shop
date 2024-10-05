function comments_accepted() {
    FlagId = 100
    tbody_comment.innerHTML=""
    comment_accepted.classList.remove('!hidden')
    orderViews.classList.add('!hidden')
    button_product_detail_view.classList.add('!hidden')
    fetch(`http://localhost:8001/comment/comments/admin-panel`, {
        method: 'GET',
    }).then(async request => {
        let comments = ''
        const pro = await request.json()
        pro.forEach(comment => {
            console.log(comment)
            comments = `     <tr>

        <td>
          <div class="flex items-center gap-3">
            <div class="avatar">
              <div class="mask mask-squircle h-12 w-12">
                <img
                  src="${comment.user.profile_image ?
                comment.user.profile_image :
                'https://via.placeholder.com/300'}"
                  alt="Avatar Tailwind CSS Component" />
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
            <textarea class="w-full h-24 resize-none" placeholder=${comment.text}></textarea>
        </div>
 
          <br />
          <span class="badge badge-ghost badge-sm">Desktop Support Technician</span>
          <button class="btn btn-ghost btn-xs" onclick="delete_comments(${comment.id})">delete</button>
          <button class="btn btn-ghost btn-xs" onclick="accept_comments(${comment.id})">accept</button>
        </th>
          <td>
          <div class="flex items-center gap-3">
            <div class="avatar">
              <div class="mask mask-squircle h-12 w-12">
                <img
                  src="${comment.product.images ?
                comment.product.images[0].image :
                'https://via.placeholder.com/300'}"
                  alt="Avatar Tailwind CSS Component" />
              </div>
            </div>
            <div>
              <div class="font-bold">${comment.product.title}</div>
              <div class="text-sm opacity-50">${comment.product.description}</div>
            </div>
          </div>
        </td>
        <td>
      </tr> `
            tbody_comment.innerHTML += comments
        })


    })


}