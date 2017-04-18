FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3 python3-dev libmysqlclient-dev curl gcc

RUN cd /tmp && \
    curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

ADD . /var/pastes-api

RUN cd /var/pastes-api && \
    pip install -e .

EXPOSE 8080

CMD cd /var/pastes-api && python3 pastes_api run