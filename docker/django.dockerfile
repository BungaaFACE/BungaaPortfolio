FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip3 install -r requirements.txt --break-system-packages
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py add_experience
RUN python manage.py add_skills

CMD ["gunicorn", "config.wsgi", "-c", "config/gunicorn.conf.py"]