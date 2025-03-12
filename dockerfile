FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Instala dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia somente o manage.py (opcional) para não ficar sem ele
COPY manage.py /app/

# Comando padrão (vai ser sobrescrito pelo docker-compose se quiser)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
