# Portfolio Website

Professional portfolio built with Python and Flask. Showcases experience, projects, skills, and certifications with a REST API backend, contact form with email delivery, and production-ready deployment.

**Live site:** [https://veeru.pythonanywhere.com/](https://veeru.pythonanywhere.com/)

---

## Tech Stack

- **Backend:** Python 3, Flask, REST API
- **Data:** Structured data layer with models and serializers
- **Security:** Rate limiting (Flask-Limiter), validation, environment-based config
- **Email:** SMTP integration for contact form
- **Frontend:** Vanilla JavaScript, responsive CSS, accessibility (ARIA, semantic HTML)
- **Deployment:** WSGI, PythonAnywhere (see [DEPLOYMENT.md](DEPLOYMENT.md))

---

## Features

- Single-page portfolio with About, Experience, Education, Skills, Projects, Certifications, and Contact
- REST API endpoints for portfolio data (projects, skills, experience, education, certifications)
- Contact form with server-side validation, email delivery, and rate limiting
- Responsive layout and mobile navigation
- Accessibility: skip link, ARIA labels, keyboard support
- Environment-based configuration; no secrets in repository
- Error handling and user-facing messages when API or email fails
- Health check endpoint for monitoring

---

## Before You Run

- Add `bannuru-veerendra-resume.pdf` and `profile.jpg` under `static/documents/` for the resume button and profile image.
- Copy `.env.example` to `.env` and set variables. For production, use a strong random `SECRET_KEY` (e.g. `openssl rand -hex 32`).

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bannuru-veerendra/Portfolio.git
cd Portfolio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python run.py
```

Runs at `http://localhost:5000` by default. Set `FLASK_RUN_HOST`, `FLASK_RUN_PORT`, and `FLASK_DEBUG` in `.env` if needed.

---

## Deployment

The application is deployed and live at **[https://veeru.pythonanywhere.com/](https://veeru.pythonanywhere.com/)**.

For step-by-step deployment (PythonAnywhere, WSGI, static files, environment variables), see **[DEPLOYMENT.md](DEPLOYMENT.md)**.

---

## Project Structure

```
Portfolio/
├── run.py                      # Application entry point
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── app/                        # Application package
│   ├── __init__.py             # Flask app factory, template/static paths
│   ├── config.py               # Configuration (env, logging)
│   ├── logger.py               # Logging setup
│   ├── exceptions.py           # Custom exceptions (e.g. ValidationError)
│   ├── extensions.py           # Flask extensions (e.g. rate limiter)
│   ├── data/
│   │   └── data.py             # Portfolio data (projects, skills, experience, etc.)
│   ├── models/
│   │   ├── models.py           # Data models
│   │   └── serializers.py      # API serializers
│   ├── routes/
│   │   ├── index.py            # Index and health check routes
│   │   ├── api.py              # API endpoints (projects, skills, experience, etc.)
│   │   └── contact.py          # Contact form submission
│   └── services/
│       └── email_service.py    # SMTP email sending
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css           # Main stylesheet
│   ├── js/
│   │   └── script.js           # Frontend logic, API loading, contact form
│   └── documents/              # Resume PDF, profile image (add these locally)
├── templates/
│   └── index.html              # Homepage
```

---

## Author

Veerendra Bannuru — [GitHub](https://github.com/bannuru-veerendra) | [LinkedIn](https://www.linkedin.com/in/veerendra-bannuru-900934215)