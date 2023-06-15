from Database.db_handler import DatabaseHandler
from Config.config import get_config
import http.server

class HtmlHandler:
    @staticmethod
    def get_username_from_sid(handler):
        sid = handler.cookies['sessionId']
        
        config = get_config()

        db_config = config['database']
        db = DatabaseHandler.getInstance(db_config['host'], db_config['dbname'], db_config['user'], db_config['password'])
        
        user_name = None
        while not user_name:
            user_name = db.fetch_query("""SELECT username FROM users WHERE sid = %s;""", (str(sid),))

        if len(user_name) != 1:
            print("found no/multiple users with same sid!!", len(user_name), sid)
            return None
        else:
            return user_name[0][0]



    @staticmethod
    def handle(handler):
        handler.path = 'Static/explore_forms.html'

        user_name = HtmlHandler.get_username_from_sid(handler)
        if user_name is None:
            handler.path = 'Static/explore_forms_nologin.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(handler)
             

        with open(handler.path) as myFile:
            content = myFile.read()
            content = str(content).replace("${{{user_name}}}", str(user_name))
            handler.send_response(200)
            handler.send_header('Content-type', 'text/html')
            handler.end_headers()
            handler.wfile.write(bytearray(content, 'utf-8'))
        return
		