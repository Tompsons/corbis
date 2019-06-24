# Pasos para instalar entorno y ejecutar app:


## Clonar repositorio

1. `git clone https://github.com/Tompsons/corbis.git`
2. Cambiarse al directorio *corbis*

### Build
```
docker-compose build
```

### Run
```
docker-compose up
```

## Migrate DB and Create User
En una segunda terminal, ejecutar:
```
docker exec -it corbis_web_1 /bin/bash

python manage.py collectstatic --no-input
python manage.py makemessages
python manage.py compilemessages
python manage.py migrate
python manage.py loaddata stock/fixtures/initial_data.json
```

Crear el usuario administrador del sistema:
`python manage.py createsuperuser`


## Consola Administración de Stock
- Abrir navegador web, y acceder a: `http://127.0.0.1:8000/`

## Sitio de administración - Django-Admin
- Acceder a `http://127.0.0.1:8000/admin/`
