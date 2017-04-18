FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3 python3-dev libmysqlclient-dev curl gcc

RUN cd /tmp && \
    curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

ADD . /var/shorten-id-api

RUN cd /var/shorten-id-api && \
    pip install -e .

EXPOSE 8080

CMD cd /var/shorten-id-api && python3 shorten_id_api run