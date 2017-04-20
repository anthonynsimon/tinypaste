FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3 python3-dev libmysqlclient-dev curl gcc

RUN cd /tmp && \
    curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

COPY . /var/pastes-api

RUN cd /var/pastes-api && \
    pip install -e .

RUN cd /tmp && \
    curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.3.0-amd64.deb && \
    dpkg -i filebeat-5.3.0-amd64.deb

COPY filebeat.yml /etc/filebeat/filebeat.yml

EXPOSE 8080

CMD /etc/init.d/filebeat start && \
    cd /var/pastes-api && python3 pastes_api run