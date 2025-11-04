## Configuration du dépôt
# Initialisation du dépôt GIT local
git config --global user.name "Sebastien"
git config --global user.email"s.andres@hizkia.eu"
git init
git add .
git commit -m "Initialisation du projet analyse de sentiment

# Lié le dépôt local à GitHub
git remote add origin https://github.com/s.andres@hizkia.eu/analyse-sentiment-api.git
git branch -M main
git push -u origin main
