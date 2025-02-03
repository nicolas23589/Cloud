# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la API
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que la API va a utilizar
EXPOSE 5000

# Comando para ejecutar la API
CMD ["python", "API.py"]
