FROM logstash

COPY logstash.conf /var/logstash/config/logstash.conf

EXPOSE 5044

CMD ["-f", "/var/logstash/config/logstash.conf"]