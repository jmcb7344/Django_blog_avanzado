# Blog completo - Django
> Este proyecto se realizo como practica de aprendizaje de las herramientas que proporciona Django. En este proyecto podras:
- Crear, editar y eliminar un Post
- Crear un usuario
- Crear un comentario para los Post (solo si estas reguistrado)
- Hacer un Like para los Post (solo si estas reguistrado)
- Se regista la cantidad de visualizaciones del post (solo si ya hizo login)

------------

![principp](https://user-images.githubusercontent.com/95278683/188040120-9498443b-d8ac-4cf5-a12d-068fe5f7b13a.png)

------------
#### Descarga e instalación de la practica
1. - Descargar: 
`$ git clone https://github.com/jmcb7344/flask_login.git`
2. - Crea el entorno virtual: 
`$ python -m venv .venv`
3. - Activa el entorno virtual: 
Win `$ .venv\Scripts\activate`
Otros `$ .venv/bin/activate`
4. - Instalación de dependencias: 
`$ pip install -r requirements.txt`
5. - Acceder a la carpeta
`$ cd src`
6. - Generar la migracion
`$ python manage.py makemigrations post`
`$ python manage.py migrate`
`$ python manage.py makemigrations post`
8. - Crear Superusuario: 
`$ python manage.py createsuperuser`
8. - Ejecución: 
`$ python manage.py runserver`

------------
![comentarios](https://user-images.githubusercontent.com/95278683/188040156-b8bf29f2-5c2d-45ed-9438-96a3ae7960d7.png)
