from http.server import BaseHTTPRequestHandler, HTTPServer
from pyisemail import is_email
import re         
import psycopg2
from datetime import datetime
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8085

con = psycopg2.connect(
    database="EMOF",
    user="postgres",
    password="s2receptor",
    host="localhost",
    port= '5432'
)

def get_max_user_id():
    cur = con.cursor()
    sql = "SELECT MAX(id) FROM users"
    cur.execute(sql)
    result = cur.fetchone()[0]
    if result == None:
        result = 0
    cur.close()
    return result

def check_if_email_already_exists(email):
    cur = con.cursor()
    sql = "SELECT COUNT(*) FROM users WHERE email = %s"
    cur.execute(sql, (email,))
    result = cur.fetchone()[0]
    cur.close()
    return result > 0

def check_if_username_already_exists(username):
    cur = con.cursor()
    sql = "SELECT COUNT(*) FROM users WHERE username = %s"
    cur.execute(sql, (username,))
    result = cur.fetchone()[0]
    cur.close()
    return result > 0
    
def insert_user(email, username, password):
    if not is_email(email, allow_gtld=False):
        raise ValueError("Invalid email address.")
    if check_if_email_already_exists(email):
        raise ValueError("Email address already exists.")
    if check_if_username_already_exists(username):
        raise ValueError("Username already exists.")

    cur = con.cursor()
    id = get_max_user_id() + 1
    now = datetime.now()
    sql = "INSERT INTO users (id, email, username, password, created_at, updated_at) " \
          "VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (id, email, username, password, now, now))
    con.commit()
    cur.close()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            filename = 'landing.html'
        else:
            filename = self.path[1:]
        try:
            with open(filename, 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'File not found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = parse_qs(body.decode('utf-8'))
        email = data['email'][0]
        username = data['username'][0]
        password = data['password'][0]
        
        try:
            insert_user(email, username, password)
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Success")
        except ValueError as e:
            self.send_response(400)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()  
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
