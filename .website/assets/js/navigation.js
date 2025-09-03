// Mobile Navigation Toggle Functionality
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.Navigation__Toggle');
    const menu = document.querySelector('.Navigation__Menu');
    
    if (toggle && menu) {
        toggle.addEventListener('click', function() {
            // Toggle active classes
            toggle.classList.toggle('Active');
            menu.classList.toggle('Active');
            
            // Update ARIA attributes
            const isExpanded = toggle.classList.contains('Active');
            toggle.setAttribute('aria-expanded', isExpanded);
            
            // Prevent body scrolling when menu is open
            document.body.style.overflow = isExpanded ? 'hidden' : '';
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!toggle.contains(event.target) && !menu.contains(event.target)) {
                toggle.classList.remove('Active');
                menu.classList.remove('Active');
                toggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });
        
        // Close menu on escape key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && toggle.classList.contains('Active')) {
                toggle.classList.remove('Active');
                menu.classList.remove('Active');
                toggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
                toggle.focus(); // Return focus to toggle button
            }
        });
        
        // Handle window resize - hide mobile menu if screen becomes larger
        window.addEventListener('resize', function() {
            if (window.innerWidth >= 768 && toggle.classList.contains('Active')) {
                toggle.classList.remove('Active');
                menu.classList.remove('Active');
                toggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });
    }
});