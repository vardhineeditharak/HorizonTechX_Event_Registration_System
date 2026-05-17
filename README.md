# Event Registration System

This is a Django-based event registration web application. It lets organizers create and manage events, while users can browse upcoming events, register for them, and cancel their registrations when needed.

The project also includes REST API endpoints, so the same backend can be used by a frontend client or tested through tools like Postman.

## What It Does

- Users can sign up, log in, and log out.
- Organizers can create, edit, and delete their own events.
- Users can view available events and register for them.
- Users can see all of their registrations in one place.
- The app prevents duplicate registrations.
- The app prevents registration when an event is full.
- Events in the past cannot be registered for.
- Admins can manage data through the Django admin panel.

## Tech Used

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL
- HTML and CSS

## Screens and Pages

The main web app includes:

| Page | URL |
| --- | --- |
| Event list | `/` |
| Sign up | `/signup/` |
| Login | `/login/` |
| Create event | `/events/new/` |
| Event details | `/events/<id>/` |
| Edit event | `/events/<id>/edit/` |
| Delete event | `/events/<id>/delete/` |
| My registrations | `/my-registrations/` |
| Admin panel | `/admin/` |

## API Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `POST` | `/api/users/signup/` | Create a new user |
| `POST` | `/api/token/` | Login and get JWT tokens |
| `POST` | `/api/token/refresh/` | Refresh JWT token |
| `GET` | `/api/events/` | List events |
| `POST` | `/api/events/` | Create an event |
| `GET` | `/api/events/<id>/` | View event details |
| `PUT/PATCH` | `/api/events/<id>/` | Update an event |
| `DELETE` | `/api/events/<id>/` | Delete an event |
| `GET` | `/api/registrations/` | View logged-in user's registrations |
| `POST` | `/api/registrations/` | Register for an event |
| `DELETE` | `/api/registrations/<id>/` | Cancel a registration |

## How to Run Locally

Clone the project and move into the folder:

```powershell
git clone <your-repository-url>
cd Event_Registration_System
```

Create a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

Create a `.env` file:

```powershell
copy .env.example .env
```

Update the `.env` file with your PostgreSQL details:

```env
DJANGO_SECRET_KEY=change-this-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB=event_registration_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-postgres-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Create the PostgreSQL database:

```sql
CREATE DATABASE event_registration_db;
```

Run migrations:

```powershell
python manage.py migrate
```

Create an admin account:

```powershell
python manage.py createsuperuser
```

Start the development server:

```powershell
python manage.py runserver
```

Open the app:

```text
http://127.0.0.1:8000/
```

## Project Structure

```text
config/             Project settings and main URL configuration
events/             Event model, forms, serializers, views, and permissions
registrations/      Registration model, serializers, and views
users/              Signup forms, serializers, and user-related views
templates/          HTML templates
static/             CSS files
```

## Notes

This project uses PostgreSQL. Local files such as `.env`, `venv/`, `__pycache__/`, and local database files are ignored using `.gitignore`.

The `.env.example` file is included only as a template. Real passwords and secret keys should stay in your local `.env` file and should not be pushed to GitHub.
