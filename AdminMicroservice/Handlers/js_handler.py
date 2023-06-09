import http.server

class JsHandler:
    @staticmethod
    def handle(handler):
        handler.path = '/Static/admin.js'
        return http.server.SimpleHTTPRequestHandler.do_GET(handler)