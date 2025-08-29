# Task Manager Application – Development Guide

## Overview

The Task Manager Application is a full-stack web platform for managing tasks, featuring user authentication, task creation, and management. The backend is built with Django and Django REST Framework, the frontend with React, and PostgreSQL is used as the database.

---

## Project Structure

```
task_manager/
├── manage.py
├── requirements.txt
├── task_manager/         # Django project settings and URLs
├── users/                # User app: models, views, serializers, URLs
├── tasks/                # Task app: models, views, serializers, URLs
├── user_app/             # (Optional/extra app)
├── frontend/             # React frontend
│   ├── src/
│   │   ├── components/   # Navbar, ProtectedRoute, etc.
│   │   ├── context/      # UserContext for auth state
│   │   ├── pages/        # HomePage, LoginPage, TaskPage, NotFoundPage
│   │   ├── services/     # api.js, auth.js for API calls
│   │   └── App.js        # Main React app
│   ├── public/
│   └── package.json
├── docs/                 # Documentation
│   └── images/
└── env/                  # Python virtual environment
```

---

## Backend (Django)

### Apps

- **users**: Custom user model (inherits from AbstractUser), registration, login, and user management.
- **tasks**: Task model, CRUD operations for tasks.
- **user_app**: (Optional, for extra features or experiments.)

### Models

- **User**: Custom user model with fields for username, email, and password. Inherits from AbstractUser for Django compatibility.
- **Task**: Linked to User via ForeignKey. Fields: title, description, completed, created_at, updated_at.

### Serializers

- **UserSerializer**: Serializes user data for API responses.
- **TaskSerializer**: Serializes task data.

### Views

- **UserViewSet**: Handles user CRUD and authentication endpoints.
- **TaskViewSet**: Handles task CRUD endpoints.

### URLs

- All API endpoints are routed via task_manager/urls.py, using Django REST Framework routers for viewsets.

### Authentication

- Uses JWT (via rest_framework_simplejwt) for secure token-based authentication.
- Registration and login endpoints issue tokens.
- Protected endpoints require the token in the Authorization header.

### Database

- PostgreSQL is configured in settings.py.
- Migrations are used to create/update tables.

---

## Frontend (React)

### Structure

- **components/**: Navbar, ProtectedRoute (checks auth before allowing access to certain pages).
- **context/UserContext.js**: Provides user state throughout the app.
- **pages/**: HomePage, LoginPage, TaskPage, NotFoundPage.
- **services/api.js**: Handles API requests, attaches JWT token to headers.
- **services/auth.js**: Handles login, logout, and fetching current user.

### Routing

- Uses React Router for navigation.
- ProtectedRoute ensures only authenticated users can access /tasks.

### Auth Flow

1. User logs in via LoginPage.
2. Token is saved to localStorage.
3. API requests include the token in the Authorization header.
4. UserContext provides user info to components.

### Task Management

- TaskPage fetches and displays tasks for the logged-in user.
- Users can create, update, and delete tasks via API.

---

## Backend-Frontend Interaction

- The frontend communicates with the backend via RESTful API endpoints (e.g., /api/login/, /api/tasks/).
- JWT tokens are used for authentication.
- All data is exchanged in JSON format.

---

## Development Workflow

### Backend

1. Create and activate a Python virtual environment.
2. Install dependencies: pip install -r requirements.txt
3. Configure PostgreSQL in settings.py.
4. Run migrations: python manage.py migrate
5. Start the server: python manage.py runserver

### Frontend

1. cd frontend
2. Install dependencies: npm install
3. Start the dev server: npm start

---

## Testing

- Backend: python manage.py test
- Frontend: npm test

---

## Extending the Project

- Add new models or features by creating new Django apps or React components.
- Use serializers and viewsets to expose new API endpoints.
- Update frontend services to consume new APIs.

---

## CI/CD

- Example GitHub Actions workflow is provided in the README for automated testing and deployment.

---

## Summary

This project is a modern, full-stack web application with a clear separation of concerns between backend and frontend. It uses best practices for authentication, API design, and frontend state management.

---

## Roadmap for Adding a New Feature

1. **Define the Feature**
   - Clearly describe the feature and its purpose.
   - Identify which part of the stack it affects (backend, frontend, or both).

2. **Design the Data Model (if needed)**
   - Update or create Django models.
   - Create or update serializers for new/changed models.

3. **Backend Implementation**
   - Add or update views (ViewSets, APIViews, etc.).
   - Register new endpoints in the Django URLs.
   - Write or update tests for backend logic.

4. **Database Migration**
   - Run `python manage.py makemigrations` and `python manage.py migrate` to apply model changes.

5. **Frontend Implementation**
   - Add or update React components/pages.
   - Update or create API service functions.
   - Connect new UI to backend endpoints.
   - Write or update frontend tests.

6. **Integration**
   - Ensure frontend and backend communicate as expected.
   - Test the full feature flow.

7. **Documentation**
   - Update docs/development.md and/or README.md with details about the new feature.
   - Add usage instructions or API documentation as needed.

8. **Code Review & Testing**
   - Review code for style and best practices.
   - Run all tests and fix any issues.

9. **Deployment**
   - Merge changes to main branch.
   - Deploy to staging/production as appropriate.

