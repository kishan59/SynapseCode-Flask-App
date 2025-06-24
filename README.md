# SynapseCode: Your Personal Code Snippet Manager

#### Video Demo:  `<URL HERE - PLEASE INSERT YOUR VIDEO DEMO URL>`

#### Live Demo:  `https://synapsecode-flask-app.onrender.com`

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
    * `app/__init__.py`: Initializes the Flask app, sets up extensions (SQLAlchemy, Flask-Login), and registers blueprints for different feature areas. This file also effectively serves as the application's entry point for the `flask run` command.
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
* `instance/`: This directory holds instance-specific files that should not be under version control.
    * `instance/config.py`: This file stores application configuration settings, including sensitive data like the `SECRET_KEY` and the local database URI. It's deliberately excluded from Git tracking (`.gitignore`) to prevent sensitive information from being exposed in the repository and to allow for different configurations in development vs. production environments.
* `requirements.txt`: Lists all Python dependencies, crucial for environment setup.
* `.gitignore`: Specifies files/directories Git should ignore (e.g., virtual environment, local database, instance folder content).

### Design Choices & Rationale

When building SynapseCode, I made several deliberate design choices:

* **Flask for Flexibility:** I chose Flask because it's a lightweight microframework. This gave me precise control over each component without unnecessary boilerplate, which was ideal for building this specific snippet management functionality.
* **SQLAlchemy for Database Management:** SQLAlchemy (with Flask-SQLAlchemy) provided a robust ORM that abstracted away direct SQL, making database interactions in Python much cleaner and safer from common vulnerabilities. For local development, SQLite was simple to use, but I know a production deployment would require a move to a more robust database like PostgreSQL for better concurrency and persistence.
* **Bootstrap 5 & Custom Dark Theme:** I opted for Bootstrap 5 to accelerate frontend development and ensure responsiveness across devices. The custom dark theme, defined in `custom.css` using CSS variables, was a personal preference to create a modern, developer-friendly interface that's easy on the eyes. This involved careful iteration to get colors and contrasts just right across all UI elements like cards, forms, and buttons.
* **Client-Side Features (Prism.js & AJAX):**
    * **Prism.js** for syntax highlighting was a clear choice to improve code readability directly in the browser. I leveraged its built-in "Copy to Clipboard" functionality, which simplified development compared to rolling my own solution, and integrated its styling into the dark theme.
    * **AJAX (Asynchronous JavaScript and XML)** requests were crucial for a smoother user experience. For actions like deleting a snippet or opening the detailed view modal, AJAX allows the UI to update immediately without a full page reload. This makes the application feel much faster and more interactive. For delete operations, it also allowed me to correctly use HTTP `POST` requests for security.
* **Organic Search Strategy:** The search functionality was designed to be highly organic, utilizing a single search input that queries multiple relevant fields (`title`, `description`, `code_content`, `notes`, `tags`). The backend logic processes keywords with `AND` logic and `ILIKE` for case-insensitivity, allowing users to type natural language queries rather than rigid syntax. This decision aims to make finding snippets as intuitive and efficient as possible, which is central to the app's usability.

### Acknowledgements

I would like to express my gratitude to the following resources and tools that were instrumental in the development of SynapseCode:

* **CS50x:** For providing the foundational knowledge in computer science, web development principles, database concepts, and guiding the overall project structure.
* **Flask:** The Python web framework.
* **Flask-SQLAlchemy:** ORM for database interactions.
* **Flask-Bcrypt:** For secure password hashing.
* **Flask-Login:** For user session management.
* **Flask-WTF:** For form handling and CSRF protection.
* **Bootstrap 5:** The responsive frontend framework.
* **Prism.js:** For client-side syntax highlighting.
* **Gunicorn:** The WSGI HTTP server for production deployment.
* **python-dotenv:** For managing local environment variables.
* **psycopg2-binary:** The PostgreSQL adapter for Python.
* **Google Gemini API:** For helping with lots of aesthetics (css) of this app.
* **Render.com:** For providing a seamless platform for deploying the application.
* **GitHub:** For version control and collaborative development.
* **Google Fonts:** For the Poppins and Fira Code typefaces used in the application's design.


This `README.md` provides a comprehensive overview of SynapseCode's purpose, features, architecture, and the thought process behind its design choices, adhering to the CS50 project guidelines.