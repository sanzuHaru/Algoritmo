# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Expone el puerto en el que la aplicación escucha
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "Server_CV.py"]
