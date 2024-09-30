const validateEmail = function(email) {
    const formData = new FormData();
    formData.append('email', email)
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/validate/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            $('.error').text(res.msg);
        }
    });
};

const subscribeUser = function(email, name) {
    var formData = new FormData();
    formData.append('email', email);
    formData.append('name', name);
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/newsletter/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            $('.success').text(res.msg);
            $('#userEmail').val(' ');
            $('#userName').val(' ');
        }
    });
};

(function ($) {
    $('#submit').on('click', () => {
        event.preventDefault();
        const userEmail = $('#userEmail').val();
        const userName = $('#userName').val();
        if (userEmail && userName) {
            subscribeUser(userEmail, userName);
        }
    });

    $('#userEmail').on('change', (event) => {
        event.preventDefault();
        const email = event.target.value;
        validateEmail(email);
    });
})(jQuery);