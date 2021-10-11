FROM python:3.8

RUN apt update && apt install pip -y && apt-get update && apt-get upgrade -y && pip3 install mysqlclient && \
apt-get install wget -y
# 도커라이징 하는 이유 -> django 서버가 먼저 실행되서 mysql을 못찾아서 도커라이징으로 기다리게 함
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["dockerize", "-wait", "tcp://mysql_service:3306", "-timeout", "20s"]

WORKDIR /app

COPY ./ ./

RUN pip install -r ./requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000