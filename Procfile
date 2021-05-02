release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: python manage.py collectstatic --no-input; gunicorn employeeapi.wsgi --log-file -