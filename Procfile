web: gunicorn config.wsgi:application
worker: celery worker --app=locmaster.taskapp --loglevel=info
