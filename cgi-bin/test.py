import cgi
import json
import os
import sys

data = json.load(sys.stdin)

with open('123.txt', 'w') as file:
    file.write(os.environ['HTTP_USER_AGENT'])
    file.write((os.environ['REMOTE_ADDR']))

