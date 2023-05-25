import os
import socketserver
from Handlers.request_handler import MyHttpRequestHandler

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8087

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()