FROM python:3.9-slim

WORKDIR /app

# Copier les fichiers de l'application
COPY . /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Définir les variables d'environnement
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
RUN pip install --upgrade pip


# Commande pour démarrer l'application
CMD ["flask", "run"]