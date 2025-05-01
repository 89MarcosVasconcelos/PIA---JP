FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala dependências do sistema e Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --retries 10 --timeout 30 -r requirements.txt

# Copia os arquivos do projeto
COPY . .

# Garante que o diretório de arquivos estáticos exista
RUN mkdir -p /app/staticfiles

# Coleta os arquivos estáticos (necessário STATIC_ROOT no settings.py)
RUN python manage.py collectstatic --noinput

# Expõe a porta usada pelo Gunicorn
EXPOSE 8000

# Inicia o Gunicorn com o WSGI do seu projeto Django
CMD ["gunicorn", "pia_project.wsgi:application", "--bind", "0.0.0.0:8000"]
