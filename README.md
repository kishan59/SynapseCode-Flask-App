# SynapseCode: Your Personal Code Snippet Manager

#### Video Demo:  `<URL HERE - PLEASE INSERT YOUR VIDEO DEMO URL>`

#### Description:

SynapseCode is a personal web application designed to solve a common developer problem: easily organizing, finding, and managing code snippets. As I built more projects, I found valuable code snippets getting lost in notes or scattered across different files. SynapseCode aims to be that single, intuitive place where I (or any developer) can save, search, and retrieve code knowledge efficiently.

My main goal with SynapseCode was to make the search experience as "organic" as possible. This means avoiding rigid search syntax and allowing users to find what they need by simply typing keywords. While it's currently version 1.0, the focus has been on building a robust foundation for this core search functionality, along with a clean, responsive, and visually appealing dark-themed interface. It's truly a personal knowledge base designed for daily use.

**Key Features Implemented:**

* **Secure User Accounts:** Users can register, log in, and manage their sessions securely.
* **Full Snippet Management (CRUD):** Easily add new code snippets with details like title, code, language, description, notes, and source URL. Snippets can be viewed in detail via a modal, and existing ones can be edited or deleted.
* **Intuitive Search & Filtering:** The central "My Snippets" page features a single search bar that searches across snippet title, code content, description, notes, and tags using `AND` logic for multiple keywords. An optional text-based language filter allows for further refinement.
* **Pagination:** Snippet listings are paginated to ensure smooth performance even with a large number of saved items.
* **Responsive UI:** Built with Bootstrap 5 to look good and function well on desktops, tablets, and mobile devices.
* **Consistent Dark Theme:** A custom dark theme using defined color variables ensures a cohesive and eye-friendly experience across the entire application.
* **Syntax Highlighting & Copy:** Code blocks feature syntax highlighting via Prism.js, and a "Copy to Clipboard" button appears on hover for convenience.

### File Breakdown

My project is structured following common Flask application best practices, promoting modularity and maintainability.

* `app/`: This is the main application package.
    * `app/__init__.py`: Initializes the Flask app, sets up extensions (SQLAlchemy, Flask-Login), and registers blueprints for different feature areas.
    * `app/auth/`: Blueprint for user authentication.
        * `app/auth/routes.py`: Handles user registration, login, and logout.
        * `app/auth/forms.py`: Defines Flask-WTF forms for authentication.
    * `app/snippets/`: Blueprint for managing code snippets.
        * `app/snippets/routes.py`: Contains routes for creating, viewing (all and individual JSON), editing, and deleting snippets. This is also where the search and pagination logic is implemented.
        * `app/snippets/forms.py`: Defines the Flask-WTF form used for adding and editing snippets.
    * `app/models.py`: Defines the SQLAlchemy database models (`User` and `Snippet`) and their relationships.
    * `app/static/`: Stores static assets.
        * `app/static/css/custom.css`: My custom CSS for the dark theme, overriding Bootstrap defaults and defining specific styles for components like cards, forms, and the Prism.js copy button.
        * `app/static/js/main.js`: Custom JavaScript for client-side interactions, including modal population, AJAX delete requests, and "Copy to Clipboard" button behavior.
        * `app/static/js/prism.js`: The Prism.js library for syntax highlighting.
    * `app/templates/`: Contains Jinja2 HTML templates.
        * `app/templates/layout.html`: The base template, defining the overall page structure, navigation, and script/stylesheet includes.
        * `app/templates/index.html`: The application's main landing page.
        * `app/templates/auth/login.html`: The login page HTML.
        * `app/templates/auth/register.html`: The registration page HTML.
        * `app/templates/snippets/my_snippets.html`: Displays the user's snippet collection, search bar, and the snippet detail modal.
        * `app/templates/snippets/add_snippet.html`: The form used for both adding new and editing existing snippets.
* `config.py`: Stores application-wide configuration settings (database URI, secret key, pagination).
* `run.py`: The entry point for starting the Flask development server.
* `requirements.txt`: Lists all Python dependencies, crucial for environment setup.
* `.gitignore`: Specifies files/directories Git should ignore (e.g., virtual environment, local database).

### Design Choices & Rationale

When building SynapseCode, I made several deliberate design choices:

* **Flask for Flexibility:** I chose Flask because it's a lightweight microframework. This gave me precise control over each component without unnecessary boilerplate, which was ideal for building this specific snippet management functionality.
* **SQLAlchemy for Database Management:** SQLAlchemy (with Flask-SQLAlchemy) provided a robust ORM that abstracted away direct SQL, making database interactions in Python much cleaner and safer from common vulnerabilities. For local development, SQLite was simple to use, but I know a production deployment would require a move to a more robust database like PostgreSQL for better concurrency and persistence.
* **Bootstrap 5 & Custom Dark Theme:** I opted for Bootstrap 5 to accelerate frontend development and ensure responsiveness across devices. The custom dark theme, defined in `custom.css` using CSS variables, was a personal preference to create a modern, developer-friendly interface that's easy on the eyes. This involved careful iteration to get colors and contrasts just right across all UI elements like cards, forms, and buttons.
* **Client-Side Features (Prism.js & AJAX):**
    * **Prism.js** for syntax highlighting was a clear choice to improve code readability directly in the browser. I leveraged its built-in "Copy to Clipboard" functionality, which simplified development compared to rolling my own solution, and integrated its styling into the dark theme.
    * **AJAX (Asynchronous JavaScript and XML)** requests were crucial for a smoother user experience. For actions like deleting a snippet or opening the detailed view modal, AJAX allows the UI to update immediately without a full page reload. This makes the application feel much faster and more interactive. For delete operations, it also allowed me to correctly use HTTP `POST` requests for security.
* **Organic Search Strategy:** The decision to implement a single, multi-field search bar with keyword `AND` logic was central to the "organic search" goal. I wanted users to be able to type naturally (e.g., "python list comprehension") and find relevant snippets without needing to learn complex query syntax. This flexible approach is key to the app's usability.

This `README.md` provides a comprehensive overview of SynapseCode's purpose, features, architecture, and the thought process behind its design choices, adhering to the CS50 project guidelines.