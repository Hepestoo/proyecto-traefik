# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de la raíz del proyecto al contenedor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para iniciar (usando Gunicorn para producción, mejor que el server dev de Flask)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]