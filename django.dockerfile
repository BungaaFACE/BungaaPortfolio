FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
RUN pip3 install -r requirements.txt --break-system-packages
RUN mkdir db
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py add_experience
RUN python manage.py add_skills
RUN python manage.py add_projects

CMD ["gunicorn", "config.wsgi", "-c", "config/gunicorn.conf.py"]