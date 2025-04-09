# Utilise une image Python officielle
FROM python:3.11

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie tous les fichiers de backend/ dans /app
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lance le serveur FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
