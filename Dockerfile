FROM python:3.10.2-slim-bullseye
COPY . /src
WORKDIR /src
RUN pip3 install -r requirements.txt
EXPOSE 80