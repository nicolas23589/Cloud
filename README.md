# Video explicativo
https://www.loom.com/share/c5cfa51451654c798b096e260d385ac9?sid=89fd19a9-e4a0-446a-86cd-591f096b7ad4
(Se utilizó loom para mayor conveniencia de visualización)

# Instrucciones de despliegue:

Se requieren como dependencias python, flask, jwt, angular y node js

Para despligue local, clonar el ropositorio, instalar dependencias, y ejecutar: 

-correr el API.py (python API.py) en la carpeta del api

-IMPORTANTE: ejecutar también el dbCreation.py

-comando ng serve en la carpeta de front 

-Luego dirigirse a localhost:4200

-Se empaquetó la app con docker, con los comandos docker-compose build y docker-compose up se construye y se ejecuta respectivamente, hasta ese punto no debería dar problemas y la consola debería arrojar que ambos procesos se completaron satisfactoriamente

-Debido a contratiempos no se realizó el despliegue en aws academy, puede que haya comportamientos inesperados al ejecutar también la app en el docker de manera local

# Decisiones

- De acuerdo a la libertad dada por el enunciado, se decidieron manejar categorías predefinidas, implementando un back completo y funcional con todos los endpoints obligatorios, los demás endpoints opcionales fueron sustituidos por un manejo en el front y sus decisiones de diseño

- Se usó el motor de base de datos sqlite3 con las tablas del modelo recomendado en el enunciado

# Autenticación

-Todos los endpoints responden (como se puede comprobar en la colección de postman, adjunta en la carpeta del api, la baseUrl se debe configurar como la http://127.0.0.1:5000, dirección por defecto donde corre el api de flask)

-Se implementaron tokens jwt, son otorgados por el api al momento del login

-Se implementó una autenticación sencilla con contraseña, usada en los métodos iniciarSesion() del back y front

# Funcionalidades
-Desde el front se puede hacer:
 
-creación de usuarios

-log in y su validación (casos positivos o mensaje de error si las credenciales son incorrectas)

-consultar tareas

-editar tareas

-borrar tareas

-crear tareas

-ver las tareas separadas por categoría

-En el front se usan el 100% de los métodos del back
