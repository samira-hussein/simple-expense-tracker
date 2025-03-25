document.addEventListener('DOMContentLoaded', function () {

    // Form Validation
    const form = document.getElementById('expense-form'); // For form has this ID
    if (form) {
        form.addEventListener('submit', function(event) {
            const name = document.getElementById('id_name');
            const amount = document.getElementById('id_amount');
            const date = document.getElementById('id_date');
            
            // Basic validation
            if (!name.value || !amount.value || !date.value) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }

    // Toggle Expense Visibility
    const toggleButtons = document.querySelectorAll('.toggle-details'); // class to the buttons

    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const details = this.nextElementSibling; // for details are right after the button
            if (details.style.display === 'none') {
                details.style.display = 'block';
                this.textContent = 'Hide Details';
            } else {
                details.style.display = 'none';
                this.textContent = 'Show Details';
            }
        });
    });

    // Delete Expense Confirmation
    const deleteButtons = document.querySelectorAll('.delete-expense'); // for delete button has this class
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this expense?')) {
                event.preventDefault(); // Prevent the link from being followed
            }
        });
    });

    // Smooth Scroll for Anchor Links
    const scrollLinks = document.querySelectorAll('a[href^="#"]'); // All links with hash-based hrefs
    
    scrollLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });
        });
    });

});
