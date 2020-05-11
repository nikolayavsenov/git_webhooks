import cgi
from datetime import datetime
from settings import *


class Header:
    def __init__(self, header):
        self.header = header

    @staticmethod
    def validate_headers(headers):
        """Валидация заголовков"""
        data_type = cgi.parse_header(headers['content-type'])
        event_type = cgi.parse_header(headers['X-Github-Event'])
        return data_type != 'application/json' and event_type != EVENT_TYPE

    #@staticmethod
    # def validate_signature(self):
    #     """Вычисление хеша и проверка подписи"""
        # signature = cgi.parse_header(self.header['X-Hub-Signature'])
        # digest = hmac.new(digestmod=hashlib.sha1, key=GIT_KEY, msg=raw_data)
        #hmac.compare_digest("sha1=" + digest.hexdigest(), signature)


class Hook:
    def __init__(self, request):
        self.received_date = datetime.now
        self.status = 'Decline'
        self.request = request

    # def validate_request(self):
    #     if self.reque


class DataHandler:
    def __init__(self, data):
        self.data = data

    def write(self):
        with open('123.txt', 'w') as file:
            file.write((str(self.data)))





