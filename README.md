# Docker Commands

Start docker
docker-compose up -d --build

1. Create an app
docker-compose exec web python manage.py startapp app_name

2. Run migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

3. Create Superuser
docker-compose exec web python manage.py createsuperuser

4. Docker Tests
docker-compose exec web python manage.py test