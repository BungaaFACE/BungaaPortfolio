#/bin/sh

rm "./db/db.sqlite3" 2> /dev/null
./.venv/bin/python manage.py migrate
./.venv/bin/python manage.py add_experience
./.venv/bin/python manage.py add_skills
./.venv/bin/python manage.py add_projects