FROM python:3.11
# Ne pas lancer les app en root dans docker
RUN useradd flask
WORKDIR /home/flask
# Copier uniquement requirements pour cache Docker
COPY requirements.txt .
RUN pip install -r requirements.txt
#Ajouter tout le contexte sauf le contenu de .dockerignore
COPY . .
# Installer les déps python, pas besoin de venv car docker

RUN chmod a+x app.py test.py && \
 chown -R flask:flask ./
# Déclarer la config de l'app
ENV FLASK_APP=app.py
EXPOSE 5000
# Changer d'user pour lancer l'app
USER flask
CMD ["./app.py"]