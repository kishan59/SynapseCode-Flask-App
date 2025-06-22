# SynapseCode: Your Personal Code Snippet Manager

#### Video Demo:  `<URL HERE - PLEASE INSERT YOUR VIDEO DEMO URL>`

#### Description:

SynapseCode is a personal web application designed to help developers efficiently organize, store, search, and manage their valuable code snippets. In the fast-paced world of software development, constantly encountering useful code snippets, solutions, or algorithms is common. Without a centralized and easily searchable system, these valuable pieces of knowledge can get lost, making it difficult to retrieve them when needed. SynapseCode addresses this challenge by providing a dedicated, intuitive platform for personal code knowledge management.

The core philosophy behind SynapseCode is to make snippet management as "organic" as possible. This means focusing on a natural, flexible user experience for storing and, critically, retrieving information. Users should be able to quickly add new snippets, complete with rich descriptions and relevant tags, and then find them effortlessly using a powerful yet simple search interface. The application prioritizes clean aesthetics and a fluid user interaction to ensure productivity. This initial version (1.0) lays a robust foundation for a comprehensive personal knowledge base, with a strong emphasis on effective search capabilities.

**Key Features Implemented:**

* **User Authentication:** Secure user registration and login functionality.
* **Snippet Creation (CRUD):** Users can add new code snippets, providing a title, the code content itself, the programming language, a detailed description, personal notes, a source URL, and relevant tags.
* **Snippet Viewing:** Snippets are displayed in a clean, card-based layout on the "My Snippets" page. Clicking a snippet opens a modal dialog for a detailed view, complete with syntax highlighting.
* **Snippet Editing:** Users can easily modify their existing snippets via a pre-filled form, ensuring their code knowledge remains up-to-date.
* **Snippet Deletion:** A streamlined process for removing unwanted or outdated snippets, with confirmation prompts for safety.
* **Organic Search & Filtering:** A central search bar allows users to query across multiple fields (title, code, description, notes, tags) using keyword-based `AND` logic, along with an optional text-based language filter for precise results.
* **Pagination:** Results on the "My Snippets" page are paginated for better performance and usability with a large number of snippets.
* **Responsive Design:** The application is built with Bootstrap 5, ensuring a responsive and consistent user interface across various devices (desktop, tablet, mobile).
* **Cohesive Dark Theme:** A custom dark theme, designed with SynapseCode's brand colors (dark blues, accent green, light text), provides a modern and visually appealing experience throughout the application.

### File Breakdown

The project follows a modular structure, typical for Flask applications, to keep concerns separated and the codebase organized.

* `app/`: This is the main application package.
    * `app/__init__.py`: Initializes the Flask application, configures extensions like SQLAlchemy and Flask-Login, and registers blueprints. This file acts as the central hub for app setup.
    * `app/auth/`: A Flask Blueprint dedicated to user authentication.
        * `app/auth/routes.py`: Contains routes for user registration (`/register`), login (`/login`), and logout (`/logout`). It handles form processing, user creation, password hashing, and session management.
        * `app/auth/forms.py`: Defines the Flask-WTF forms for user registration and login, including validation rules for fields like username and password.
    * `app/snippets/`: A Flask Blueprint for managing code snippets.
        * `app/snippets/routes.py`: Houses routes for adding (`/snippet/new`), viewing all (`/my_snippets`), viewing individual snippet JSON (`/snippets/<int:snippet_id>/json`), editing (`/snippet/<int:snippet_id>/edit`), and deleting (`/snippet/<int:int:snippet_id>/delete`) snippets. This is where the search and pagination logic resides.
        * `app/snippets/forms.py`: Defines the Flask-WTF form for creating and editing code snippets, with fields for title, code content, language, description, notes, source URL, and tags.
    * `app/models.py`: Defines the SQLAlchemy database models for `User` and `Snippet`. It establishes the relationships between users and their snippets (one-to-many).
    * `app/static/`: Contains static assets served directly to the browser.
        * `app/static/css/custom.css`: This is the heart of SynapseCode's custom dark theme. It defines all the custom color variables, overrides Bootstrap defaults, and provides specific styling for cards, forms, buttons, alerts, and the Prism.js copy button, ensuring a consistent and branded look.
        * `app/static/js/main.js`: Contains custom client-side JavaScript for interactive elements. Key functionalities include dynamically populating the snippet detail modal, handling the "Copy to Clipboard" feature, and making the card-level delete button interactive via AJAX.
        * `app/static/js/prism.js`: The JavaScript library for client-side syntax highlighting of code blocks.
    * `app/templates/`: Stores all the Jinja2 HTML templates.
        * `app/templates/layout.html`: The base template extended by all other pages. It defines the common structure, including the HTML head, navigation bar, flash message display area, main content block, and footer. It also links to all CSS and JavaScript files.
        * `app/templates/index.html`: The application's homepage, displaying a welcoming hero section and an overview of the app's features.
        * `app/templates/auth/login.html`: The user login form.
        * `app/templates/auth/register.html`: The new user registration form.
        * `app/templates/snippets/my_snippets.html`: Displays a user's collection of code snippets, including the search/filter bar, the card-based layout, and the hidden modal for detailed snippet viewing.
        * `app/templates/snippets/add_snippet.html`: The form used for both adding new snippets and editing existing ones, dynamically adjusting its title based on context.
* `config.py`: Contains the application's configuration settings, such as the database URI, `SECRET_KEY`, and pagination settings (e.g., `POSTS_PER_PAGE`).
* `run.py`: The entry point for the Flask application. It creates the Flask app instance and runs the development server.
* `requirements.txt`: Lists all Python dependencies required by the project. This is essential for deployment, allowing the hosting environment to install the correct packages.
* `.gitignore`: A crucial file that specifies which files and directories Git should ignore (e.g., virtual environments, database files, cache files, IDE-specific files). This ensures a clean and secure repository.

### Design Choices & Rationale

Throughout the development of SynapseCode, several design decisions were made to balance functionality, user experience, and development efficiency:

* **Flask as the Backend Framework:** Flask was chosen for its lightweight nature and flexibility. It provides a solid microframework foundation, allowing us to build the application's core logic without the overhead of a full-stack framework, enabling precise control over components.
* **SQLite for Local Development:** For ease of initial setup and local development, SQLite was used as the database. Its file-based nature simplifies environment setup without requiring external database servers. However, it's acknowledged that for production deployment, a more robust database like PostgreSQL will be necessary to handle data persistence and concurrent access reliably.
* **Flask-SQLAlchemy for ORM:** This extension simplifies database interactions by providing an Object-Relational Mapper (ORM), allowing Python objects to represent database rows. This abstracts SQL queries, making the code cleaner and less error-prone.
* **Flask-Login for Authentication:** Flask-Login manages user sessions, handling login, logout, and restricting access to protected routes, significantly streamlining authentication implementation.
* **Flask-WTF for Forms:** This extension was chosen for its robust form handling and built-in CSRF (Cross-Site Request Forgery) protection. It simplifies form creation, validation, and rendering, enhancing both security and developer productivity.
* **Bootstrap 5 for Frontend Framework:** Bootstrap provides a powerful, responsive, and mobile-first CSS framework. It accelerates UI development by offering pre-built components and a utility-first approach, ensuring the application looks good on any device.
* **Custom Dark Theme (`custom.css`):** A deliberate choice was made to implement a custom dark theme using CSS variables (`:root`). This allows for easy management of brand colors and ensures a consistent visual identity across the entire application, providing a modern and eye-friendly interface for developers. The iterative process of refining colors for different elements (cards, forms, buttons, alerts) was essential to achieve visual harmony and readability against varying backgrounds.
* **Prism.js for Syntax Highlighting:** Implementing client-side syntax highlighting was critical for code readability. Prism.js was selected for its ease of integration, lightweight nature, and extensibility. The decision to use its built-in "Copy to Clipboard" plugin (after an initial attempt at a custom JS solution) was driven by its simplicity and automatic handling of copy logic and UI feedback.
* **AJAX for Delete and Modal View:** Instead of relying on full-page reloads for actions like deleting a snippet or viewing details in a modal, AJAX (Asynchronous JavaScript and XML) was used. For deletion, this provides a smoother user experience where the snippet card vanishes instantly without a page refresh, while also enforcing the secure HTTP `POST` method on the backend. The modal also leverages AJAX to fetch snippet data on demand, keeping the initial page load fast. This choice improves the perceived performance and responsiveness of the application.
* **"Organic Search" Implementation:** The search functionality was designed to be highly organic, utilizing a single search input that queries multiple relevant fields (`title`, `description`, `code_content`, `notes`, `tags`). The backend logic processes keywords with `AND` logic and `ILIKE` for case-insensitivity, allowing users to type natural language queries rather than rigid syntax. This decision aims to make finding snippets as intuitive and efficient as possible, which is central to the app's value proposition.

This `README.md` provides a comprehensive overview of SynapseCode's purpose, features, architecture, and the thought process behind its design choices, adhering to the CS50 project guidelines.