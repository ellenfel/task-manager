# Contributing to Task Manager

Thank you for your interest in contributing to the Task Manager project! This document provides guidelines and instructions for contributing to the project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/ellenfel/task_manager.git
   cd task_manager
   ```

## Development Setup

### Backend Setup
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Making Changes

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the style guide

3. Test your changes thoroughly

4. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

## Pull Request Process

1. Ensure your code follows the style guide
2. Update the README.md with details of changes if needed
3. Update the documentation if needed
4. The PR must pass all tests
5. You may merge the PR once you have the sign-off of at least one other developer

## Style Guide

### Python (Backend)
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### JavaScript/React (Frontend)
- Use functional components with hooks
- Follow ESLint rules
- Use meaningful component and variable names
- Keep components focused and small
- Use PropTypes for component props

### Git Commit Messages
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

## Testing

### Backend Testing
```bash
python manage.py test
```

### Frontend Testing
```bash
cd frontend
npm test
```

## Documentation

- Keep documentation up to date
- Use clear and concise language
- Include examples where appropriate
- Document all new features and changes

## Questions?

If you have any questions, feel free to:
- Open an issue


Thank you for contributing to Task Manager! 