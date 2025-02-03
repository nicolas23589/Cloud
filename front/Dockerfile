# Usar una imagen base de Node.js
FROM node:14

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del frontend
COPY ./ /app

# Instalar dependencias
RUN npm install

# Construir la aplicación Angular para producción
RUN ng build

# Exponer el puerto en el que el frontend estará disponible
EXPOSE 80

# Comando para servir la aplicación Angular
CMD ["npx", "http-server", "dist", "--port", "80"]
