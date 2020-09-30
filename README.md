# Docker Commands

1. Start docker
docker-compose up -d --build

2. Create an app
docker-compose exec web python manage.py startapp app_name

3. Run migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

## Create Superuser
docker-compose exec web python manage.py createsuperuser

## Docker Tests
docker-compose exec web python manage.py test

## See the logs
docker-compose logs 

## Restart the server
docker-compose down
docker-compose up -d

