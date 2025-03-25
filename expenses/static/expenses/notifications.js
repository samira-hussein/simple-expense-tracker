// static/expenses/notifications.js

// Function to fetch new notifications
function fetchNotifications() {
    fetch('/notifications/')
        .then(response => response.json())
        .then(data => {
            const notificationsDiv = document.getElementById('notifications');
            
            // Clear existing notifications
            notificationsDiv.innerHTML = '';

            // If there are new notifications, display them
            if (data.notifications.length > 0) {
                data.notifications.forEach(notification => {
                    const notificationElement = document.createElement('div');
                    notificationElement.textContent = notification.message;
                    notificationsDiv.appendChild(notificationElement);
                });
            }
        })
        .catch(error => console.error('Error fetching notifications:', error));
}

// Poll for new notifications every 10 seconds (10000 milliseconds)
setInterval(fetchNotifications, 10000);
