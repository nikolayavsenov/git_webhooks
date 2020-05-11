import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from handl import *


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        return self.send_error(500, 'denied')
        #block_on_fw(ip)

    def do_POST(self):
        if Header.validate_headers(self.headers):
            return print("Valid")
        data_type = cgi.parse_header(self.headers['content-type'])
        event_type = cgi.parse_header(self.headers['X-Github-Event'])
        raw_data = self.rfile.read(int(self.headers['content-length']))
        data = json.loads(raw_data)
        """Проверка заголовков"""
        test = DataHandler(data)
        test.write()
        print("Event:", event_type[0])


def start_server(port):
    http_server = HTTPServer(('', int(port)), RequestHandler)
    http_server.serve_forever()


if __name__ == "__main__":
    start_server(8080)
