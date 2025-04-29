# Usa uma imagem do Python
FROM python:3.12.6

# Evita criação de arquivos .pyc e faz logs saírem direto no console
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho no container
WORKDIR /app

# Copia só o requirements primeiro (para aproveitar o cache em rebuilds)
COPY requirements.txt /app/

# Instala as dependências
RUN pip install --no-cache-dir --upgrade pip \
    && pip install -r requirements.txt

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Coleta arquivos estáticos (se aplicável)
RUN python manage.py collectstatic --noinput

# Expõe a porta do Gunicorn
EXPOSE 8000

# Comando para rodar o Gunicorn no container
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pia_project.wsgi:application"]
