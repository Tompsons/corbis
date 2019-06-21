# Build
-------
```
docker-compose build
```

# Run
-----
```
docker-compose up
```

# Migrate DB and Create User
----------------------------
```
docker exec -it corbis_web_1 /bin/bash

python manage.py collectstatic --no-input
python manage.py makemessages
python manage.py compilemessages
python manage.py migrate
python manage.py createsuperuser
```
