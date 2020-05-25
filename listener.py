import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from handl import *


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        log = Logger(self.headers, self.client_address[0], 'GET request')
        log.record_event()
        return self.send_error(500, 'denied')
        # TODO: log to file, block_on_fw(ip)

    def do_POST(self):
        raw_data = self.rfile.read(int(self.headers['content-length']))
        headers = Header(self.headers, raw_data)
        if headers.validate():
            data = json.loads(raw_data)
            task_giver = TaskGiver()
            task_giver.start_event(data)
        else:
            self.send_error(400, 'invalid_headers')
            log = Logger(self.headers, self.client_address[0], 'Invalid headers')
            log.record_event()
            # TODO: log to file, block on fw


def start_server(port):
    http_server = HTTPServer(('', int(port)), RequestHandler)
    http_server.serve_forever()


if __name__ == "__main__":
    start_server(8080)
