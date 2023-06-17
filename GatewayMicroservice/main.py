import http.server
import requests
import urllib.parse
import json

from http.server import ThreadingHTTPServer
from http.cookies import SimpleCookie

# acest gateway va prelua cererea clientului si va trimite cererea catre serviciul aferent , gateway ul asteapta
# raspunsul de la serviciul aferent si dupa ce il primeste il trimite inapoi la client
# 
# de ex : 
# clientul face request la http://127.0.0.1:8050/forms-microservice (8050 fiind portul acestui gateway , forms-microservice e serviciul aferent la care vrem sa trimitem request)
# acest gateway va prelua cererea cererea clientului si o va trimite catre http://127.0.0.1:8088 (acesta este URL-ul la care serviciul aferent a fost pornit) 
# , gateway ul va returna automat catre client raspunsul de la http://127.0.0.1:8088

SERVICE_URLS = {
    'forms-microservice': 'http://127.0.0.1:8088',  # asta inseamna ca de acum requesturile catre http://127.0.0.1:8050/forms-microservice vor fi redirectate catre  http://127.0.0.1:8088
    'admin-forms-microservice' : "http://127.0.0.1:8100" ,
    'admin': 'http://127.0.0.1:8090',
    'explore': 'http://127.0.0.1:8091',
    'service2': 'http://127.0.0.1:5002',
    'authentication': 'http://127.0.0.1:8084',
    'statistics': 'http://127.0.0.1:8083'
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

    def do_PUT(self):
        self.handle_request(requests.put)

    def handle_request(self, request_method):
        url = urllib.parse.urlparse(self.path)
        segments = url.path.split('/')[1:]  # split by / and remove the first empty string
        service = segments[0]

        #get cookie data
        data = {}
        cookie_raw = self.headers.get('Cookie')
        if cookie_raw:
            print(cookie_raw)
            cookie = SimpleCookie()
            cookie.load(cookie_raw)
            print(cookie)
            cookies = {k: v.value for k, v in cookie.items()}
            data.update({"cookie" : cookies})

        if 'Content-Length' in self.headers:
            content_length = int(self.headers['Content-Length'])  # Get the size of data
            raw_data = self.rfile.read(content_length)  # Get the data itself
            raw_data_decoded = raw_data.decode('utf-8')
            data_json = json.loads(raw_data_decoded)
            #combine cookie data with the data from client header request
            data.update(data_json)
    
        forward_data = bytearray(json.dumps(data),"utf-8")

        if service in SERVICE_URLS:
            target_url = SERVICE_URLS[service] + '/' + '/'.join(segments[1:])
            if url.query != "":
                target_url = target_url + "?" + url.query
            
            print("UITE FRATE ::")
            print(forward_data)
            response = request_method(target_url, data=forward_data)

            self.send_response(response.status_code)
            self.end_headers()
            self.wfile.write(response.content)

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Service not found')


PORT = 8050

with ThreadingHTTPServer(("", PORT), GatewayRequestHandler) as httpd:
    print("Gateway service running at port", PORT)
    httpd.serve_forever()