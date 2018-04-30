FROM python:3.6-alpine
ADD . /app
WORKDIR /app

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN pip install -r requirements.txt
CMD ["python", "/app/web/app.py"]