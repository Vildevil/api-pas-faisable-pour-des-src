FROM python:3.11
WORKDIR /app

copy . .


RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run" ]

