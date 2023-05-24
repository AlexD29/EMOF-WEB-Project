import http.server

class JsonHandler:
    @staticmethod
    def handle(handler, id=None):
        
        handler.path = '/Static/Questions/' + id + '.json'
        return http.server.SimpleHTTPRequestHandler.do_GET(handler)