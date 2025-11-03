# 🐍 Python Quiz Platform

A modern web application for practicing Python programming with multiple choice and coding questions.

## Features

- 📝 **Multiple Choice Questions**: Test your Python knowledge with comprehensive MCQ questions
- 💻 **Coding Questions**: Practice coding with real-time execution and test case validation
- ✅ **Instant Feedback**: Get immediate feedback on your answers
- 📊 **Difficulty Levels**: Questions ranging from easy to hard
- 🎨 **Modern UI**: Beautiful, responsive interface built with React

## Tech Stack

### Backend
- Django 5.2.7
- Django REST Framework
- django-cors-headers

### Frontend
- React 19
- React Router
- Axios
- Vite

## Setup Instructions

### Prerequisites
- Python 3.14 or higher
- Node.js 16+ and npm

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies (using uv if available, or pip):
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install django djangorestframework django-cors-headers
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

5. Populate the database with questions:
```bash
python manage.py populate_questions
```

6. Start the Django development server:
```bash
python manage.py runserver
```

The backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend/react
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

## Usage

1. Start both the backend and frontend servers
2. Open your browser and navigate to `http://localhost:5173`
3. Choose between Multiple Choice or Coding questions
4. Answer questions and get instant feedback!

## API Endpoints

- `GET /api/questions/` - List all questions (supports ?type=, ?difficulty=, ?category= filters)
- `GET /api/questions/random/` - Get a random question (supports ?type= filter)
- `POST /api/questions/{id}/check_answer/` - Check answer for a question
  - For multiple choice: `{"choice_id": 1}`
  - For coding: `{"code": "your code here"}`
- `GET /api/categories/` - List all categories

## Adding More Questions

You can add questions in two ways:

1. **Using the management command**: Edit `backend/quiz/management/commands/populate_questions.py` and run it again
2. **Using Django Admin**: 
   - Create a superuser: `python manage.py createsuperuser`
   - Access admin panel at `http://localhost:8000/admin`
   - Add questions, choices, and test cases through the admin interface

## Project Structure

```
Python-quizz/
├── backend/
│   ├── main/           # Django project settings
│   ├── quiz/           # Quiz app
│   │   ├── models.py   # Database models
│   │   ├── views.py    # API views
│   │   ├── serializers.py
│   │   └── management/commands/populate_questions.py
│   └── manage.py
├── frontend/
│   └── react/
│       └── src/
│           ├── pages/  # React pages
│           ├── utils/  # API utilities
│           └── App.jsx
└── README.md
```

## Notes

- The coding question execution runs Python code safely on the server
- Test cases are used to validate coding solutions
- Questions are stored in SQLite by default (can be changed in settings.py)

## Contributing

Feel free to add more Python questions or improve the UI/UX!

