bind = f'0.0.0.0:8080'
workers = 8
loglevel = 'DEBUG'
accesslog = '/data/logs/gunicorn_access.log'
errorlog = '/data/logs/gunicorn_error.log'