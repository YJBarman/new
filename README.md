# Hindi-English Learning App

A web application for practicing Hindi-English translations with features like hints, practice mode, and sentence management.

## Features

- Practice Hindi to English translations
- Progressive hint system (reveals one word at a time)
- Skip difficult sentences
- Add new sentence pairs
- View all sentences in the database

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Visit http://localhost:5000 in your browser

## Deployment

This application is ready to be deployed on Render.com. Follow these steps:

1. Create a free account on [Render](https://render.com)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the deployment:
   - Name: hindi-english-practice (or your preferred name)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click "Create Web Service"

The application will be automatically deployed and available at your Render URL.
