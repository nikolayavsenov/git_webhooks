import cgi
import hashlib
import hmac
from settings import *


class Header:
    """Обработка заголовков"""
    def __init__(self, header, raw_data):
        self.header = header
        self.raw_data = raw_data

    def validate(self):
        return self.validate_headers() #and self.validate_signature():

    def validate_headers(self):
        """Валидация"""
        try:
            data_type = cgi.parse_header(self.header['content-type'])
            event_type = cgi.parse_header(self.header['X-Github-Event'])
            print(event_type != EVENT_TYPE)
            return data_type != 'application/json' and event_type != EVENT_TYPE
        except Exception:
            return False

    def validate_signature(self):
        """Вычисление хеша и проверка подписи"""
        signature = cgi.parse_header(self.header['X-Hub-Signature'])
        digest = hmac.new(digestmod=hashlib.sha1, key=GIT_KEY, msg=self.raw_data)
        hmac.compare_digest("sha1=" + digest.hexdigest(), signature)


class Event:
    def __init__(self, task_type):
        self.task_type = task_type


class NullHandler:
    """Обарботчик задач"""
    def __init__(self, successfully=None):
        self.__successfully = successfully

    def task_assigner(self, data, event):
        if self.__successfully is not None:
            self.__successfully.handle(data, event)


class BackendUpdate(NullHandler):
    """Задача на обновление бэка"""
    def handle(self, data, event):
        # TODO: backend update task
        if data['repository']['full_name'] == BACKEND_URL:
            print('Starting backend update!')
        else:
            super().task_assigner(data, event)


class FrontendUpdate(NullHandler):
    """Задача на обновление фронта"""
    def handle(self, data, event):
        if data['repository']['full_name'] == FRONTEND_URL:
            # TODO: frontend update task
            print('Starting frontend update!')
        else:
            super().task_assigner(data, event)


class TaskGiver:
    """Менеджер задач"""
    def __init__(self):
        self.handlers = FrontendUpdate(BackendUpdate(NullHandler))
        self.events = []

    def start_event(self, event):
        if event['repository']['full_name'] == FRONTEND_URL:
            self.events.append(Event(FrontendUpdate))
        elif event['repository']['full_name'] == BACKEND_URL:
            self.events.append(Event(BackendUpdate))
        self.handle_tasks(event)

    def handle_tasks(self, data):
        for event in self.events:
            self.handlers.handle(data, event)
