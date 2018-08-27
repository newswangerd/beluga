FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./

ENV FLASK_APP="main.py"

CMD [ "flask", "run", "--host=0.0.0.0" ]

EXPOSE 5000

HEALTHCHECK CMD curl --fail http://localhost:5000/health
