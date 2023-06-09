from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import psycopg2

hostName = "localhost"
serverPort = 8081

con = psycopg2.connect(
    database="EMOF",
    user="postgres",
    password="s2receptor",
    host="localhost",
    port='5432'
)


class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/StatisticsMicroservice/statistics.html'
        elif self.path == '/data':
            id_form = 1
            form_name = self.get_form_name(id_form)
            data = self.retrieve_data_from_database(id_form)
            for item in data:
                item['form_name'] = form_name
            response_data = {'form_name': form_name, 'data': data}
            response = json.dumps(response_data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.end_headers()
            self.wfile.write(response)
            return
        return SimpleHTTPRequestHandler.do_GET(self)

    def retrieve_data_from_database(self, id_form):
        cur = con.cursor()
        cur.execute(f"SELECT q.text, STRING_AGG(r.emotion, '|') FROM questions q JOIN responses r ON q.id = r.id_question WHERE q.id_form = {id_form} GROUP BY q.text")
        rows = cur.fetchall()
        cur.close()

        data = [{'question': row[0], 'answers': row[1].split('|')} for row in rows]

        return data

    def get_form_name(self, id_form):
        cur = con.cursor()
        cur.execute(f"SELECT name FROM forms WHERE id = {id_form}")
        result = cur.fetchone()
        cur.close()

        if result:
            form_name = result[0]
            return form_name

        return None




if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
