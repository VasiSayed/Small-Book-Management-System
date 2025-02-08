# Book Management System

## Overview

(venv) C:\IT Vedant\My Modules\Django Framwork\Book\_Ass>pip freeze>requirements.txt &#x20;

Access is denied.Features

- **User Authentication**: Register, log in, and log out.
- **Book Management**: Add, view, update, and delete books.
- **Database**: Uses PostgreSQL or SQLite.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/book-management.git
   cd book-management/backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/register/` - Register a new user
- `POST /api/login/` - Log in a user
- `GET /api/logout/` - Log out a user
- `GET /api/books/` - List books
- `POST /api/books/` - Add a book
- `GET /api/books/<id>/` - View book details
- `PUT /api/books/<id>/` - Update a book
- `DELETE /api/books/<id>/` - Delete a book

## License

MIT License.

