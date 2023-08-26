web: gunicorn core.wsgi --log-file -
web: daphne -b 0.0.0.0 -p $PORT core.asgi:application