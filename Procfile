release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
python manage.py collectstatic --dry-run --noinput

web: gunicorn olx_demo.wsgi.py