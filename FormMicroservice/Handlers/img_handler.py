import http.server

class ImgHandler:
    @staticmethod
    def handle(handler):
        
        if handler.path.endswith("background.jpg"):
            handler.path = '/Static/background.jpg'
        else:
            handler.path = ''
        return http.server.SimpleHTTPRequestHandler.do_GET(handler)