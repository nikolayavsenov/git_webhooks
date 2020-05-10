from http.server import HTTPServer, CGIHTTPRequestHandler
import cgitb, cgi, os
import json

#webdir = "cgi-bin/"
#os.chdir(webdir)
server_address = ("", 3115)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()

def do_POST():
    data = cgi.FieldStorage()

    print(data)


