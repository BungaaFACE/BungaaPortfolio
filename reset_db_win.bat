del ".\db\db.sqlite3" 2>nul
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py add_experience
.\.venv\Scripts\python manage.py add_skills
.\.venv\Scripts\python manage.py add_projects