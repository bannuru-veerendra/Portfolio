# Portfolio Website

A modern portfolio website built with Flask, showcasing projects, skills, and professional experience.

## Planned Features

- Clean and responsive design
- Fast and lightweight Flask backend
- Rate limiting for API protection
- Compression for optimized performance
- Environment-based configuration
- Modular Flask app using application factory pattern

## Before you run

- **Resume & profile image:** Add `bannuru-veerendra-resume.pdf` and `profile.jpg` under `static/documents/` so the Download Resume button and About photo work. Create the folder if it doesn't exist.
- **Production:** Set a strong, unique `SECRET_KEY` in `.env` (e.g. `openssl rand -hex 32`). Do not use the default from `.env.example`.

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

The application will be available at `http://localhost:5000`

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

## Development

This project is in active development. More features and improvements are coming soon.

## Author

Created by [bannuru-veerendra](https://github.com/bannuru-veerendra)