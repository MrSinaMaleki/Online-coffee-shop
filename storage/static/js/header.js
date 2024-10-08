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

    // Close submenus when clicking outside the menu
    document.addEventListener('click', function(e) {
        const isClickInsideMenu = e.target.closest('nav');
        if (!isClickInsideMenu) {
            closeAllSubmenus();
        }
    });

    // Open/close the submenus
    const menuItems = document.querySelectorAll('nav > ul > li > a');
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent default link behavior
            const submenu = this.nextElementSibling; // Get the corresponding submenu
            if (submenu) {
                const isHidden = submenu.classList.contains('hidden');
                closeAllSubmenus(); // Close all submenus before toggling the selected one
                if (isHidden) {
                    submenu.classList.remove('hidden'); // Open the submenu
                }
            }
        });
    });

    function closeAllSubmenus() {
        const allSubmenus = document.querySelectorAll('.submenu, .subsubmenu');
        allSubmenus.forEach(submenu => {
            submenu.classList.add('hidden');
        });
    }
});

