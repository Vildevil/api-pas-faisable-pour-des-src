FROM python:3.11
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Assurez-vous que FLASK_APP est défini, remplacez 'app.py' par le point d'entrée de votre application Flask
ENV FLASK_APP=app.py

CMD ["flask", "run"]