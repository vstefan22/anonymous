web: gunicorn core.wsgi --log-file -
daphne -b 0.0.0.0 -p 8001 core.asgi:application