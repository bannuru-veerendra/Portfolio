# Portfolio Website

A modern portfolio website built with Flask, showcasing projects, skills, and professional experience.

## Planned Features

- Clean and responsive design
- Fast and lightweight Flask backend
- Rate limiting for API protection
- Compression for optimized performance
- Environment-based configuration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mr-veeru/Portfolio.git
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
├── run.py              # Application entry file
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── .env.example        # Environment variables template
├── README.md           # Project documentation
├── app/                # Application package
│   ├── __init__.py     # Flask application factory
│   ├── config.py       # Application configuration
│   ├── logger.py       # Logging configuration
│   └── routes/         # Route handlers
│        └── index.py   # Index and health check routes
├── static/               # Static files
│   ├── css/            # Stylesheets
│   │   └── style.css   # Main stylesheet
│   └── js/             # JavaScript files
│       └── script.js   # Main JavaScript file
└── templates/          # HTML templates
    └── index.html      # Homepage template
```

## Development

This project is in active development. More features and improvements are coming soon.

## Author

Created by [bannuru-veerendra](https://github.com/bannuru-veerendra)