from http.server import BaseHTTPRequestHandler, HTTPServer
from pyisemail import is_email
import requests        
import psycopg2
import hashlib
import os
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

def check_if_email_match_password(email,password):
    cur = con.cursor()
    sql = "SELECT password FROM users WHERE email = %s"
    cur.execute(sql, (email,))
    account_password = cur.fetchone()[0]
    cur.close()
    if account_password == password:
        return True
    else:
        return False
    
def check_if_username_match_password(username,password):
    cur = con.cursor()
    sql = "SELECT password FROM users WHERE username = %s"
    cur.execute(sql, (username,))
    account_password = cur.fetchone()[0]
    cur.close()
    if account_password == password:
        return True
    else:
        return False

def login_user(username_or_email,password):
    if check_if_email_already_exists(username_or_email):
        if check_if_email_match_password(username_or_email,password) == False:
            raise ValueError("Your password is incorrect. Re-enter your information or reset your password.")
    elif check_if_username_already_exists(username_or_email):
        if check_if_username_match_password(username_or_email,password) == False:
            raise ValueError("Your password is incorrect. Re-enter your information or reset your password.")
    else:
        raise ValueError("Your username, email, or password is incorrect. Re-enter your information or reset your password.")

def insert_user(email, username, password):
    if not is_email(email, allow_gtld=False):
        raise ValueError("Invalid email address.")
    if check_if_email_already_exists(email):
        raise ValueError("Email address already exists.")
    if check_if_username_already_exists(username):
        raise ValueError("Username already exists.")

    cur = con.cursor()
    now = datetime.now()
    sql = "INSERT INTO users (email, username, password, created_at, updated_at) " \
          "VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql, (email, username, password, now, now))
    con.commit()
    cur.close()

# def hash_password(password):
#     salt = os.urandom(16)
#     hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
#     return salt + hashed_password

# def check_password(password, hashed_password):
#     salt = hashed_password[:16]
#     new_hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
#     return hashed_password == salt + new_hashed_password

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

        if self.path == '/signup':
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
        elif self.path == '/login':
            username_email = data['emailUsername'][0]
            password = data['password'][0]

            try:
                login_user(username_email,password)
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Success")
            except ValueError as e:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        elif self.path == '/reset':
            email = data['email'][0]

            try:
                print("Reset succesfully")
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Success")
            except ValueError as e:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_error(404, 'Page not found')

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()  
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
