## Simple Expense Tracker

This is a simple expense tracker application built using Django for backend logic and basic frontend HTML/CSS. It allows users to track their expenses by categorizing them, adding a description, and viewing a list of their expenses. The project includes user authentication, so users can securely log in, register, and manage their expenses.

---

## Table of Contents

- [Project Overview](#project-overview)
- [User Design / UI / UX: Ideal User Profile](#user-design--ui--ux-ideal-user-profile)
- [Features](#features)
- [Tech stack](#tech-stack)
- [Project scope](#project-scope)
- [Technical Issues and Scope Creep](#technical-issues-and-scope-creep)
- [Future Improvements](#future-improvements)
- [AI Utilisation in Development: Impact on Workflow](#ai-utilisation-in-development-impact-on-workflow)
- [Project Resources](#project-resources)
- 
---

## Project Overview

This project was built as a basic expense tracker to help users manage their financial data. Users can log in, register, and track their expenses in different categories. It includes basic functionality such as adding, editing, and deleting expenses. The app also uses the Django framework and leverages Django's built-in user authentication system.

---
## User Design / UI / UX: Ideal User Profile

The Simple Expense Tracker is designed for individuals who need an easy and efficient way to track their daily expenses. The ideal user is someone who values simplicity, clarity, and accessibility in financial management. This includes students, young professionals, freelancers, and budget-conscious individuals who want a straightforward tool without unnecessary complexity.

From a UI/UX perspective, the design will focus on a clean, minimalistic layout with an intuitive interface. Users should be able to quickly add, edit, delete, and review expenses with minimal effort. The colour scheme will be calm and neutral, ensuring readability and reducing visual clutter. Navigation will be simple and logical, with clear buttons and input fields. The design will also be mobile-friendly, allowing users to manage expenses on the go.

The goal is to provide a smooth, user-friendly experience that makes expense tracking effortless and encourages users to develop better financial habits without feeling overwhelmed.


---

## Features

- **User Authentication**: Users can log in, log out, and register new accounts.
- **Expense Management**: Users can add, edit, and delete their expenses.
- **Expense Categories**: Users can categorize their expenses with predefined categories like "Groceries," "Rent," "Travel," etc.
- **Data Validation**: Ensures that amounts are valid and above a minimum threshold (greater than £0.01).

---

## Tech stack

### langues :
- HTML frontend 
- CSS  frontend 
- JS   frontend
- Django (Python) backend 

---

### Project scope 

The Simple Expense Tracker is a web application designed to help users efficiently manage their daily expenses. Built using Django (Python) for the backend, along with HTML, CSS, and JavaScript for the frontend, the application provides a user-friendly interface for adding, editing, deleting, and viewing expenses. Users can categorise their expenses, set budgets, and track spending over time. The project will utilise PostgreSQL as the database for securely storing expense records. Deployment will be managed via Heroku, ensuring accessibility from anywhere. Additionally, version control will be handled using GitHub, with a clear README file to document setup instructions and project details. The focus is on simplicity, ensuring ease of use while maintaining essential CRUD functionality.

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
- **UI/design**: Improve the UI (CSS styling, better buttons, layout).

- **Unit Tests**: Writing unit tests for key parts of the application (e.g., form validation, views) could ensure the application works smoothly and prevent issues during
 future development.

**Main probmlems I faced**
- technical issues, like Heroku deployment problems and static files not loading. Debugging authentication took extra time.

---

## AI Utilisation in Development: Impact on Workflow 

During the development of the Simple Expense Tracker, I relied on ChatGPT to resolve technical challenges efficiently, avoiding unnecessary code rewrites. Instead of manually debugging complex errors, I used precise prompts to identify issues, understand their root causes, and implement effective solutions.

ChatGPT played a crucial role in debugging, identifying syntax errors, missing dependencies, and configuration issues, which streamlined the development process. It also helped with code optimisation, suggesting best practices for structuring Django views, models, and database queries.

By integrating ChatGPT into my workflow, I significantly reduced development time, improved code quality, and maintained a smoother workflow, allowing me to focus on building a functional and user-friendly application.

---

## Project Resources


The following resources were used during my project:

 **YouTube Channels**:
- [Net Ninja](https://www.youtube.com/@NetNinja)
- [Coding Entrepreneurs](https://www.youtube.com/@CodingEntrepreneurs)
- [Edutechional](https://www.youtube.com/@edutechional)

 **Learning Management System (LMS)**:
- Code Institute

 **AI Assistance**:
- ChatGPT for additional understanding and support

---

**Notes**: 

- The project focused on backend functionalities using Django and simple frontend design. It can be expanded further to include more interactive and dynamic features with JavaScript and other frontend technologies.
