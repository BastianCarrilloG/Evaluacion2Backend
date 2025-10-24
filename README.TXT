Evaluación N°2 – Programación Backend 

Instrucciones de instalación:

Clonar el repositorio desde GitHub:
https://github.com/BastianCarrilloG/Evaluacion2Backend

cd inventarioEscolar

Crear y activar un entorno virtual:
python -m venv venv
venv\Scripts\actívate


Instalar dependencias:
pip install Django

Ejecutar migraciones:
python manage.py makemigrations
python manage.py migrate

Crear un superusuario:
python manage.py createsuperuser

Iniciar el servidor:
python manage.py runserver
Luego ingresar en el navegador a:
http://127.0.0.1:8000/admin/



Credenciales superadmin: Evaluacion
contraseña superadmin: Evaluacion1234


