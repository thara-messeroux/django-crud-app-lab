# TrailTales 🌵

TrailTales is a Django CRUD web app for saving, organizing, and reflecting on Joshua Tree trail discoveries. Users can log in, create their own nature journal entries, add safety and preservation notes, categorize discoveries, tag them with reusable labels, and manage their personal trail collection.

This project was built as a General Assembly Django CRUD lab and extended with stronger product thinking, user ownership, one-to-many relationships, many-to-many relationships, polished UI, and a Joshua Tree-inspired visual system.

## Live Local Pages

When the server is running, these pages are available locally:

* Home: http://127.0.0.1:8000/
* Discoveries Index: http://127.0.0.1:8000/discoveries/
* Add Discovery: http://127.0.0.1:8000/discoveries/new/
* Login: http://127.0.0.1:8000/accounts/login/
* Signup: http://127.0.0.1:8000/accounts/signup/
* Admin Dashboard: http://127.0.0.1:8000/admin/

Dynamic discovery pages use an ID:

* Discovery Detail: http://127.0.0.1:8000/discoveries/1/
* Edit Discovery: http://127.0.0.1:8000/discoveries/1/edit/
* Delete Discovery: http://127.0.0.1:8000/discoveries/1/delete/

## Project Concept

TrailTales turns a hiking experience into a thoughtful digital nature journal. Instead of only tracking objects, the app encourages users to document what they saw, where they saw it, how to stay safe, and how to protect fragile desert ecosystems.

Example discoveries include:

* Desert tortoise sightings
* Joshua Tree landscapes
* Cactus blooms
* Rock formations
* Scenic viewpoints
* Night sky moments
* Safety reminders
* Preservation notes

## Key Features

* User authentication with signup, login, and logout
* User-owned discovery data
* Full CRUD functionality for discoveries
* Create, view, edit, and delete trail discoveries
* One-to-many relationship between users and discoveries
* One-to-many relationship between categories and discoveries
* Many-to-many relationship between discoveries and tags
* Protected category relationship to prevent accidental data loss
* Django admin dashboard for managing categories, tags, and discoveries
* Joshua Tree-inspired responsive UI
* Pexels image URLs for polished visual discovery cards
* Safety and preservation fields to support responsible hiking
* Clean form handling with Django ModelForms
* Local PostgreSQL database

## Technologies Used

* Python
* Django
* PostgreSQL
* Psycopg2
* Pipenv
* HTML
* CSS
* Django Templates
* Django ORM
* Django Authentication
* Django Admin
* Git
* GitHub
* Pexels image URLs

## Languages Used

* Python
* HTML
* CSS
* SQL through Django ORM
* Markdown

## Data Model Overview

TrailTales uses three core app models: Category, Tag, and Discovery. It also uses Django's built-in User model for authentication and ownership.

### User

A user owns discoveries. Each logged-in user only sees and manages their own discoveries.

Relationship:

```text
One User → Many Discoveries
```

Example:

```text
User: thara
├── Hidden Valley Sunset
├── Desert Tortoise Crossing
└── Night Desert Sky
```

### Category

A category gives each discovery one main organizing label.

Relationship:

```text
One Category → Many Discoveries
```

Example:

```text
Category: Animal
├── Desert Tortoise Crossing
└── Roadrunner Trail Moment
```

Each discovery belongs to one category.

### Tag

Tags are reusable labels that can connect to many discoveries.

Relationship:

```text
Many Discoveries ↔ Many Tags
```

Example:

```text
Hidden Valley Sunset
├── scenic
├── sunset
└── safety

Night Desert Sky
├── scenic
├── stargazing
└── safety
```

The same tag can be used across many discoveries, and each discovery can have many tags.

## CRUD Functionality

TrailTales supports full CRUD for discoveries:

| Action | Description               | Route                       |
| ------ | ------------------------- | --------------------------- |
| Create | Add a new trail discovery | `/discoveries/new/`         |
| Read   | View all discoveries      | `/discoveries/`             |
| Read   | View one discovery        | `/discoveries/<id>/`        |
| Update | Edit a discovery          | `/discoveries/<id>/edit/`   |
| Delete | Delete a discovery        | `/discoveries/<id>/delete/` |

## Authentication and Ownership

TrailTales uses Django authentication. Users must be logged in to view, add, edit, or delete discoveries.

The app protects user data by filtering discoveries by the logged-in user:

```python
Discovery.objects.filter(user=request.user)
```

Detail, edit, and delete views also require ownership:

```python
get_object_or_404(Discovery, id=discovery_id, user=request.user)
```

This prevents users from accessing or changing another user's discoveries.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/thara-messeroux/django-crud-app-lab.git
cd django-crud-app-lab
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Start the virtual environment

```bash
pipenv shell
```

Or run commands through Pipenv directly:

```bash
pipenv run python manage.py check
```

### 4. Create the PostgreSQL database

```bash
createdb trailtales
```

If the database already exists, you can continue.

### 5. Run migrations

```bash
pipenv run python manage.py migrate
```

### 6. Create a superuser

```bash
pipenv run python manage.py createsuperuser
```

### 7. Run the development server

```bash
pipenv run python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Useful Development Commands

Check the project for Django issues:

```bash
pipenv run python manage.py check
```

Create migrations after model changes:

```bash
pipenv run python manage.py makemigrations
```

Apply migrations:

```bash
pipenv run python manage.py migrate
```

Run the local server:

```bash
pipenv run python manage.py runserver
```

Open the Django shell:

```bash
pipenv run python manage.py shell
```

View current Git status:

```bash
git status
```

Commit changes:

```bash
git add .
git commit -m "your commit message"
git push
```

## Local Test Account

For local testing, this project may include a development user:

```text
Username: thara
Password: trailtales123
```

This account is for local development only and should not be used in production.

## Smoke Test Summary

A smoke test was used to confirm the core app flow works:

```text
Login works: True
Create status: 302
Discovery created: True
Tags connected after create: ['test-safety', 'test-scenic']
Detail page status: 200
Edit status: 302
Discovery updated: True
Tags connected after edit: ['test-scenic']
Delete status: 302
Discovery deleted: True
```

This confirms:

* Login works
* Create works
* Detail page works
* Edit works
* Delete works
* Many-to-many tags save correctly
* The app does not crash during the core user flow

## Design Direction

The interface uses a Joshua Tree-inspired visual system with:

* Warm desert neutrals
* Clay and sand tones
* Rounded discovery cards
* Liquid-glass inspired surfaces
* Responsive layouts
* Visual discovery cards using image URLs
* Clear safety and preservation callouts

The goal was to make the project feel more like a thoughtful product than a basic CRUD assignment.

## Software Engineering Practices

This project follows several important software engineering practices:

* Clear model relationships
* Authentication-protected routes
* User-owned data access
* Reusable templates
* Organized static CSS
* Django ModelForms for safer form handling
* Admin customization for easier content management
* Conventional Git commits
* Incremental testing after major changes
* Smoke testing for the main CRUD flow

## Product Thinking

TrailTales is designed around three user goals:

* Remember what was discovered on the trail
* Stay safe while exploring desert environments
* Respect and preserve fragile natural spaces

This makes the app more meaningful than a simple collection tracker. It connects software engineering with UX, environmental awareness, and personal journaling.

## Future Improvements

Potential next steps:

* Add image upload support instead of image URLs
* Add search and filtering by category or tag
* Add public/private discovery settings
* Add map locations for trail discoveries
* Add favorite discoveries
* Add weather or trail condition notes
* Add accessibility audit improvements
* Deploy the app online

## Project Status

Current status:

* Core Django CRUD complete
* Authentication complete
* User ownership complete
* One-to-many relationships complete
* Many-to-many relationship complete
* Admin dashboard complete
* Smoke test passed
* Ready for final manual browser testing and polish

## Author

Built by Thara Messeroux.

* GitHub: https://github.com/thara-messeroux
* Project Repository: https://github.com/thara-messeroux/django-crud-app-lab
