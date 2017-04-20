import logging
import datetime

from flask import request


class CustomFormatter(logging.Formatter):
    converter=datetime.datetime.utcfromtimestamp
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            s = ct.strftime('%Y-%m-%dT%H:%M:%SZ')
        return s

def create_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        CustomFormatter('[%(levelname)s] %(asctime)s %(message)s')
    )
    return stream_handler

def create_file_handler(out_path):
    file_handler = logging.FileHandler(out_path)
    file_handler.setFormatter(
        CustomFormatter('[%(levelname)s] %(asctime)s %(message)s')
    )
    return file_handler

def log_requests(app):
    @app.after_request
    def after_request(response):
        app.logger.info('{code} {latency} {clientip} {method} {path}'.format(
            code=response.status_code,
            latency="100ms",
            clientip=request.remote_addr,
            method=request.method,
            path=request.full_path
        ))
        return response