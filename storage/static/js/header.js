document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();

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

    function updateCartCount() {
        fetch('http://localhost:8001/order/api/numberofproduct', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            },
        })
        .then(response => response.json())
        .then(data => {
            const cartCountElement = document.getElementById('cart-count');
            cartCountElement.textContent = data.item_count !== undefined ? data.item_count : '0';
        })
        .catch(error => console.error('Error fetching cart count:', error));
    }

    document.addEventListener('click', function(e) {
        const isClickInsideMenu = e.target.closest('nav');
        if (!isClickInsideMenu) {
            closeAllSubmenus();
        }
    });

    const menuItems = document.querySelectorAll('nav > ul > li > a');
    menuItems.forEach(item => {
        const submenu = item.nextElementSibling;

        // Prevent default behavior only if submenu exists
        if (submenu) {
            item.addEventListener('click', function(e) {
                e.preventDefault(); // Prevent default link behavior
                const isHidden = submenu.classList.contains('hidden');
                closeAllSubmenus(); // Close all submenus before toggling the selected one
                if (isHidden) {
                    submenu.classList.remove('hidden'); // Open the submenu
                }
            });
        }
    });

    function closeAllSubmenus() {
        const allSubmenus = document.querySelectorAll('.submenu, .subsubmenu');
        allSubmenus.forEach(submenu => {
            submenu.classList.add('hidden');
        });
    }
});