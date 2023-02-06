FROM python:3.10.2-slim-bullseye
ENV DB_PROD mongodb://gen_user:rt2igdpmo9@194.26.138.125:27017/default_db?authSource=admin&directConnection=true
COPY . /src
WORKDIR /src
RUN pip3 install -r requirements.txt
EXPOSE 80