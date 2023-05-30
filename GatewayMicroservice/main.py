import http.server
import socketserver
import requests
import json
import urllib.parse

from my_logging import Logger
from http.server import ThreadingHTTPServer

SERVICE_URLS = {
    'forms-microservice': 'http://127.0.0.1:8088',
    'service2': 'http://127.0.0.1:5002',
    # etc...
}

class GatewayRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.handle_request(requests.get)

    def do_POST(self):
        self.handle_request(requests.post)

    def do_PATCH(self):
        self.handle_request(requests.patch)
    
    def do_DELETE(self):
        self.handle_request(requests.delete)

    def handle_request(self, request_method):
        url = urllib.parse.urlparse(self.path)
        segments = url.path.split('/')[1:]  # split by / and remove the first empty string
        service = segments[0]

        post_data = None
        if 'Content-Length' in self.headers:
            content_length = int(self.headers['Content-Length'])  # Get the size of data
            post_data = self.rfile.read(content_length)  # Get the data itself

        if service in SERVICE_URLS:
            target_url = SERVICE_URLS[service] + '/' + '/'.join(segments[1:])
            response = request_method(target_url, data=post_data)

            self.send_response(response.status_code)
            self.end_headers()
            self.wfile.write(response.content)

            # Log the time when the response is sent
            Logger.log(self.client_address[0], f'"{self.command} {self.path} {self.request_version}"', response.status_code)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Service not found')

            # Log the time when the response is sent
            Logger.log(self.client_address[0], f'"{self.command} {self.path} {self.request_version}"', 404)


PORT = 8050

with ThreadingHTTPServer(("", PORT), GatewayRequestHandler) as httpd:
    print("Gateway service running at port", PORT)
    httpd.serve_forever()