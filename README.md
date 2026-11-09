# Django Uni Models

A small Django practice project created as part of the Developer Akademie. It models a simple university system with students, student ID cards, semesters, courses, course descriptions and professors. The goal is to practice defining Django models and their relationships (one-to-one, one-to-many and many-to-many) as well as `on_delete` behavior and `choices`. The project contains only models, with no views, templates or URLs.

## Quickstart

### Prerequisites

- Python 3.15.0
- Django 6.1.3 (installed via `requirements.txt`)

### Setup

Run these commands from the project root (the folder containing `manage.py`).

Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux, activate it with `source .venv/bin/activate` instead.

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The Django project is called `core` and the app containing the models is called `uni`. Create and apply the database migrations from the project root:

```bash
python manage.py makemigrations
python manage.py migrate
```

If `makemigrations` reports "No changes detected", check that `"uni"` is listed in `INSTALLED_APPS` in `core/settings.py`.

Since the project has no views and no admin setup, the models can be tried out in the Django shell:

```bash
python manage.py shell
```

```python
from uni.models import Professor, Semester, Kurs

professor = Professor.objects.create(first_name="Ada", last_name="Lovelace")
```