
# Instrucciones de despliegue:

Se requieren como dependencias python, flask, y node js

Para despligue local, clonar el ropositorio, instalar dependencias, ejecutar ng serve en la carpeta de front y correr el API.py en la carpeta del api

-Se empaquetó la app con docker, con los comandos docker-compose build y docker-compose up se construye y se ejecuta respectivamente
Debido a contratiempos no se realizó el despliegue en aws academy

# Decisiones

- De acuerdo a la libertad dada por el enunciado, se decidieron manejar categorías predefinidas, implementando un back completo y funcional con todos los endpoints obligatorios, los demás endpoints opcionales fueron sustituidos por un manejo en el front y sus decisiones de diseño

- Se usó el motor de base de datos sqlite3 con las tablas del modelo recomendado en el enunciado

# Autenticación

-Todos los endpoints responden (como se puede comprobar en la colección de postman, adjunta en la carpeta del api, la baseUrl se debe configurar como la http://127.0.0.1:5000, dirección por defecto donde corre el api de flask)
-Se implementaron tokens jwt, son otorgados por el api al momento del login
-Se implementó una autenticación sencilla con contraseña, usada en los métodos iniciarSesion() del back y front

# Funcionalidades
-Desde el front se puede hacer creación de usuarios, log in, consultar, editar, borrar y crear tareas y verlas separadas por categoría. Se usan el 100% de los métodos del back