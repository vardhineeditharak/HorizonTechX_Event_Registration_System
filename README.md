# Event Registration System

A Django web application and REST API for creating events, browsing upcoming events, and managing user registrations.

## Features

- User signup, login, and logout
- JWT authentication for API usage
- Event listing, search, filtering, and detail pages
- Organizer event creation, editing, and deletion
- User event registration and cancellation
- Capacity checks to prevent overbooking
- Validation for past events and invalid capacity
- Django admin panel
- PostgreSQL database support

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL
- HTML/CSS templates

## Project Structure

```text
config/             Django project settings and root URLs
events/             Event models, forms, API views, and web views
registrations/      Registration models, API views, and web views
users/              Signup/login related forms, serializers, and views
templates/          Django HTML templates
static/             CSS and static assets
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a local `.env` file from `.env.example` and update the PostgreSQL password:

```powershell
copy .env.example .env
```

This project reads configuration from environment variables. On Windows PowerShell, you can set them manually before running Django:

```powershell
$env:DJANGO_SECRET_KEY="your-local-secret-key"
$env:DJANGO_DEBUG="True"
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost"
$env:POSTGRES_DB="event_registration_db"
$env:POSTGRES_USER="postgres"
$env:POSTGRES_PASSWORD="your-postgres-password"
$env:POSTGRES_HOST="localhost"
$env:POSTGRES_PORT="5432"
```

Create the PostgreSQL database if it does not exist:

```sql
CREATE DATABASE event_registration_db;
```

Run migrations:

```powershell
python manage.py migrate
```

Create an admin user:

```powershell
python manage.py createsuperuser
```

Start the server:

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Main Web Routes

| Route | Description |
| --- | --- |
| `/` | Event list, search, and filtering |
| `/signup/` | Create a user account |
| `/login/` | Login |
| `/logout/` | Logout |
| `/events/new/` | Create event |
| `/events/<id>/` | Event details and registration action |
| `/events/<id>/edit/` | Edit organizer-owned event |
| `/events/<id>/delete/` | Delete organizer-owned event |
| `/my-registrations/` | Current user's registrations |
| `/admin/` | Django admin panel |

## API Routes

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/api/users/signup/` | Create user |
| `POST` | `/api/token/` | Get JWT access and refresh token |
| `POST` | `/api/token/refresh/` | Refresh JWT token |
| `GET` | `/api/events/` | List events |
| `POST` | `/api/events/` | Create event |
| `GET` | `/api/events/<id>/` | Event details |
| `PUT/PATCH` | `/api/events/<id>/` | Update organizer-owned event |
| `DELETE` | `/api/events/<id>/` | Delete organizer-owned event |
| `GET` | `/api/registrations/` | List current user's registrations |
| `POST` | `/api/registrations/` | Register for an event |
| `DELETE` | `/api/registrations/<id>/` | Cancel registration |

## GitHub Notes

Do not commit local-only files such as:

- `venv/`
- `.env`
- `db.sqlite3`
- `staticfiles/`
- `__pycache__/`

The `.gitignore` file already excludes these.
