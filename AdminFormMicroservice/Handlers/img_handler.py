import http.server

class ImgHandler:
    @staticmethod
    def handle(handler):
        
        if handler.path.endswith("logo.png"):
            handler.path = '/Static/logo.png'
        else:
            handler.path = ''
        return http.server.SimpleHTTPRequestHandler.do_GET(handler)