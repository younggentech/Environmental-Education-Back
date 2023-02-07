FROM python:3.10.2-slim-bullseye
COPY . /src
WORKDIR /src
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD [ "uvicorn", "app.server.app:app", "--host", "0.0.0.0"]