# Python_Blog

**A simple blog application built with Python as the backend.** This is the developer’s first blogging project using Python, featuring templated front-end and form handling. ([github.com](https://github.com/Thunderer9506/Python_Blog))

---

## Table of Contents

- [Python\_Blog](#python_blog)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Project Structure](#project-structure)
  - [Installation \& Setup](#installation--setup)
  - [Usage](#usage)
  - [Live Site](#live-site)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

---

## Project Overview

Python_Blog is a lightweight blogging application developed with Python using Flask Framework. It allows admin to create, edit, and display blog posts with form integration and templating functionality.

---

## Features

- Blog post creation, editing, and display interface  
- Form handling for user submissions (via `forms.py`)  
- HTML templating for rendering blog pages (in `templates/`)  
- Static assets handling (CSS, JavaScript) served from `static/`  
- `Procfile` suggests deployment capability (e.g., to Heroku)

---

## Architecture

- **Backend:** Python application (`main.py`) handling routing, data storage, and logic  
- **Templates:** HTML files under `templates/`, rendering dynamic content  
- **Static Files:** CSS and other assets under `static/` for styling and frontend behavior  
- **Form Processing:** Managed via `forms.py` for clean form handling  
- **Deployment Script:** `Procfile` hints at possible hosting on platforms like Heroku

---

## Project Structure

```
Python_Blog/
├── main.py
├── forms.py
├── requirements.txt
├── Procfile
├── templates/
│   └── [HTML template files]
├── static/
│   └── [CSS, images, JS files]
└── .gitignore
```

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Thunderer9506/Python_Blog.git
   cd Python_Blog
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```
   The blog should now be accessible via `http://localhost:5000` (or another default port).

---

## Usage

- Navigate to the provided local URL in your browser.  
- Interact with the blog interface—create, edit, or view posts as designed.  
- The `forms.py` module handles input validation and processing, while templates render pages dynamically.

---

## Live Site

**Live Demo:**  
*(Add your live site URL here, e.g., Heroku, Netlify, Railway, or another host)*

Example:
```
https://your-app-name.herokuapp.com
```

---

## Technologies Used

- **Python** — Backend logic and server  
- **Flask (or your framework)** — Routing and application framework (assumed)  
- **HTML & CSS** — Frontend templating and styling  
- **forms.py** — Handles form creation and validation  
- **Procfile** — For deployment to platforms like Heroku  
- Other dependencies listed in `requirements.txt`

---

## Contributing

Contributions are most welcome!  
- Fork the repo  
- Create your feature branch (`git checkout -b feature/new-feature`)  
- Commit your changes (`git commit -m "Add some feature"`)  
- Push to the branch (`git push origin feature/new-feature`)  
- Open a Pull Request for review

---

## License

*(Specify your license, e.g., MIT License. If not decided yet, you might write: "License not yet specified. Contact the maintainer for details.")*

---

## Contact

- **Developer:** Thunderer9506  
- **GitHub:** [Thunderer9506/Python_Blog](https://github.com/Thunderer9506/Python_Blog)  
- **LinkedIn:** [Code.py](https://www.linkedin.com/in/shaurya-srivastava001/)