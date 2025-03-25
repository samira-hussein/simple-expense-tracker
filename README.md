## Simple Expense Tracker

This is a simple expense tracker application built using Django for backend logic and basic frontend HTML/CSS. It allows users to track their expenses by categorizing them, adding a description, and viewing a list of their expenses. The project includes user authentication, so users can securely log in, register, and manage their expenses.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation Instructions](#installation-instructions)
- [Technical Issues and Scope Creep](#technical-issues-and-scope-creep)
- [Future Improvements](#future-improvements)
- [Licensing](#licensing)

---

## Project Overview

This project was built as a basic expense tracker to help users manage their financial data. Users can log in, register, and track their expenses in different categories. It includes basic functionality such as adding, editing, and deleting expenses. The app also uses the Django framework and leverages Django's built-in user authentication system.

---

## Features

- **User Authentication**: Users can log in, log out, and register new accounts.
- **Expense Management**: Users can add, edit, and delete their expenses.
- **Expense Categories**: Users can categorize their expenses with predefined categories like "Groceries," "Rent," "Travel," etc.
- **Data Validation**: Ensures that amounts are valid and above a minimum threshold (greater than £0.01).

---

## Installation Instructions

### Prerequisites:
- Python 3.x
- Django 4.x
- A local database or SQLite for testing.

### Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository/expense-tracker.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://127.0.0.1:8000/`

---

## Technical Issues and Scope Creep

During the development of this project, there were several technical issues that caused the project to go over scope:

- **Styling Issues**: The CSS styling was initially simple, but I encountered challenges making the user interface (UI) more polished, especially when it came to form elements and layouts.
- **JavaScript Integration**: I initially planned to use JavaScript for real-time notifications and interactive charts (pie charts, graphs). However, due to time constraints and technical issues, this was not implemented.
- **Form Validation**: I needed to ensure proper form validation and user-friendly error messages, which required extensive testing and troubleshooting.
- **Backend Functionality**: The app initially didn't include adequate handling for various edge cases (e.g., ensuring amounts were above a minimum threshold). These were addressed with additional logic and model constraints.

These issues caused the project to expand beyond the initial scope, as more time was spent troubleshooting and refining the user experience.

---

## Future Improvements

While the current version of the project is functional, here are some potential improvements that could be made to enhance the user experience and project functionality:

- **JavaScript Charts**: Integrating JavaScript charts (such as Pie Charts or Bar Graphs) would allow users to visualize their expenses. This can be done by using libraries like [Chart.js](https://www.chartjs.org/).
- **Real-Time Notifications**: Adding real-time notifications about changes to the data (new expenses, deleted expenses) could improve user interaction. This can be achieved through technologies like WebSockets or AJAX polling.
- **Exporting Data**: Implementing the ability to export data (e.g., CSV, PDF) could be useful for users who want to analyze their expenses outside of the app.
- **Expense Summary**: A summary view showing monthly or yearly spending totals per category could give users more insights into their finances.
- **Unit Tests**: Writing unit tests for key parts of the application (e.g., form validation, views) could ensure the application works smoothly and prevent issues during future development.

---

## Licensing

This project is open-source and available under the [MIT License](LICENSE).

---

**Notes**: 

- The project focused on backend functionalities using Django and simple frontend design. It can be expanded further to include more interactive and dynamic features with JavaScript and other frontend technologies.
- Make sure to keep the `static` files (like CSS, JS) in their correct locations for proper rendering.
 simple-expense-tracker