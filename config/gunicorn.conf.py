bind = f'0.0.0.0:8000'
workers = 8
loglevel = 'DEBUG'
accesslog = '/data/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = '/data/error.log'