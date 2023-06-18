from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import re
import psycopg2
import yaml

hostName = "127.0.0.1"
serverPort = 8083

def get_db_connection():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    conn = psycopg2.connect(
        database=config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
    )
    return conn
con = get_db_connection()

#Extinde SimpleHTTPRequestHandler
class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if re.match("^/([a-zA-Z0-9-_]{16})/?$",self.path): #verifica daca am /{id_form}
            id_form = self.path.split("/")[1] #Imi ia id_form-ul
            print(id_form)
            
            #Deschide pe pagina de statistici si inlocuieste placeholder-ul din HTML cu adevarul id_form
            with open('static/statistics.html') as myFile:
                content = myFile.read()
                content = str(content).replace("${{{id_form}}}", str(id_form))
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytearray(content, 'utf-8'))
            return
        elif re.match("^/data/([a-zA-Z0-9-_]{16})/?$",self.path):
            id_form = self.path.split("/data/")[1]
            data = self.retrieve_data_from_database(id_form)
            response = json.dumps(data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0') #Previne caching-ul 
            self.end_headers()
            self.wfile.write(response)
            return
        
        return SimpleHTTPRequestHandler.do_GET(self) #Daca nu intra in niciun if codul se intoarce la comportamentul default al lui do_GET
 
    def retrieve_data_from_database(self, id_form):
        cur = con.cursor()
        sql = "SELECT name, questions, published_at, closed_at FROM forms WHERE id = %s"
        cur.execute(sql, (id_form,))
        result = cur.fetchone()
        cur.close()
        
        if result:
            form_name = result[0]
            form_data = result[1]
            published_at = result[2]
            closed_at = result[3]

            questions = form_data['questions']
            
            cur = con.cursor()
            sql = "SELECT response, duration, submitted_at FROM responses WHERE id_form = %s"
            cur.execute(sql, (id_form,))
            response_rows = cur.fetchall()
            cur.close()
            
            answers = []
            for response_row in response_rows:
                response = response_row[0]
                response_duration = response_row[1]
                submitted_at = response_row[2]
                
                info = response.pop("userInfo")

                answer_data = {
                    'response': response,
                    'user_info': info,
                    'duration': str(response_duration),
                    'submitted_at': str(submitted_at)
                }
                
                answers.append(answer_data)
            
            published_at_str = published_at.strftime("%Y-%m-%d %H:%M:%S")
            closed_at_str = closed_at.strftime("%Y-%m-%d %H:%M:%S")

            last_key, requested = questions.popitem()
            
            return {
                'form_name': form_name,
                'published_at': published_at_str,
                'closed_at': closed_at_str,
                'answers': answers,
                'questions':questions,
                'requested': requested
            }
        else:
            return None

if __name__ == "__main__":
    webServer = ThreadingHTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
