import http.server

class CssHandler:
    @staticmethod
    def handle(handler):
        #Poisonous Null Byte attack & ../ ca sa nu iasa din folder
        if not(handler.path.find("%00") != -1 or handler.path.find("..") != -1):
            handler.path = '/Static/' + handler.path.split('/')[1]
            return http.server.SimpleHTTPRequestHandler.do_GET(handler)
        else:
            return None