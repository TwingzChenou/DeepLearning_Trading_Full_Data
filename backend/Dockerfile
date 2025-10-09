# backend/Dockerfile

# Utilise une image officielle de Node.js
FROM node:18

# Crée un dossier de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de config en premier (pour le cache Docker)
COPY package*.json ./

# Installe les dépendances
RUN npm install

# Copie tout le reste du code backend
COPY . .

# Expose le port utilisé par ton app
EXPOSE 3001

# Démarre l’application
CMD ["node", "server.js"]