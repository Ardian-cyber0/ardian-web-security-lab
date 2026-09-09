from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json
import hashlib


class SecurityLabHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            try:
                with open("index.html", "rb") as f:
                    content = f.read()

                self.send_response(200)
                self.send_header(
                    "Content-Type",
                    "text/html; charset=utf-8"
                )
                self.send_header(
                    "Content-Length",
                    str(len(content))
                )
                self.end_headers()

                self.wfile.write(content)

            except FileNotFoundError:
                self.send_error(
                    404,
                    "index.html tidak ditemukan"
                )

        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/login":
            length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(length).decode()
            data = parse_qs(body)

            username = data.get("username", [""])[0]
            password = data.get("password", [""])[0]

            try:
                with open("users.json", "r") as f:
                    users = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                users = {}

            user = users.get(username)

            if user is None:
                self.send_response(401)
                self.send_header(
                    "Content-Type",
                    "text/html; charset=utf-8"
                )
                self.end_headers()
                self.wfile.write(
                    b"<h1>Login gagal</h1>"
                )
                return

            salt = user["salt"]
            stored_hash = user["password_hash"]

            calculated_hash = hashlib.sha256(
                (salt + password).encode()
            ).hexdigest()

            if calculated_hash == stored_hash:
                print(f"Login berhasil: {username}")

                self.send_response(200)
                self.send_header(
                    "Content-Type",
                    "text/html; charset=utf-8"
                )
                self.end_headers()
                self.wfile.write(
                    b"<h1>Login berhasil</h1>"
                )

            else:
                print(f"Login gagal: {username}")

                self.send_response(401)
                self.send_header(
                    "Content-Type",
                    "text/html; charset=utf-8"
                )
                self.end_headers()
                self.wfile.write(
                    b"<h1>Login gagal</h1>"
                )

        else:
            self.send_error(404)


server = HTTPServer(
    ("127.0.0.1", 8000),
    SecurityLabHandler
)

print(
    "Security Lab berjalan di "
    "http://127.0.0.1:8000"
)

server.serve_forever()
