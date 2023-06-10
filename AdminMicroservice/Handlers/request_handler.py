import http.server
import re
import json

from Handlers.html_handler import HtmlHandler
from Handlers.css_handler import CssHandler
from Handlers.js_handler import JsHandler
from Handlers.img_handler import ImgHandler
from Handlers.form_list_handler import FormListHandler

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        
        #prefix is empty for the moment
        prefix = ""
        id_regex = '([a-zA-Z0-9\-_]{16})'

        self.routes = [
            # GET routes
            ('GET', f'^{prefix}/?$', HtmlHandler.handle),
            ('GET', f'^{prefix}/([^.]+).css$', CssHandler.handle),
            ('GET', f'^{prefix}/admin.js$', JsHandler.handle),
            ('GET', f'^{prefix}/pictures/([^.]+).jpg$', ImgHandler.handle),
            ('GET', f'^{prefix}/pictures/([^.]+).png$', ImgHandler.handle),

            # Microservice routes

            ('GET', f'^{prefix}/admin-api/users/{id_regex}/forms/?(\?(.*))?$', FormListHandler.handle_form_list),
            ('GET', f'^{prefix}/admin-api/forms/?(\?(.*))?$', FormListHandler.handle_explore_form_list),
            # DELETE routes
            ('DELETE', f'^{prefix}/admin-api/forms/{id_regex}/?$', FormListHandler.handle_delete_form),
            # PATCH routes
            ('PATCH', f'^{prefix}/admin-api/forms/{id_regex}/?$', FormListHandler.handle_update_form),
        ]
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')

    def do_DELETE(self):
        self.handle_request('DELETE')

    def do_PATCH(self):
        self.handle_request('PATCH')

    def handle_request(self, method):
        for route_method, pattern, handler in self.routes:
            if route_method == method:
                match = re.match(pattern, self.path)
                if match:
                    #try:
                    handler(self, **match.groupdict())
                    #except Exception as e:
                    #    exc_type, _, exc_tb = sys.exc_info()
                    #    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    #    print(exc_type, fname, exc_tb.tb_lineno)

                    #    self.send_response(500)
                    #    self.end_headers()
                    return
        self.send_response(404)
        self.end_headers()
    
    def send_json_response(self, data, status=200):
        response_data_json = json.dumps(data)
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response_data_json.encode())

    
    def send_html_response(self, data , status=200):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes(data, "utf8"))
