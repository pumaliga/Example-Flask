bind = '192.168.1.69:5000'
backlog = 2048
workers = 1
worker_class = 'eventlet'
worker_connections = 1000
timeout = 30
keepalive = 2
user = "aleksandr"
spew = False
errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
proc_name = 'Example-Flask'

venv = '/Users/macmini/PycharmProjects/Example/venv'

#  gunicorn "app:create_app()" -c gunicorn_conf.py

# pkill -f gunicorn