#!/usr/bin/python3.13
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Serve a specific HTML file
        return super().do_GET()

host = "localhost"
port = 8000

server = HTTPServer((host, port), MyHandler)
print(f"Serving on http://{host}:{port}")

server.serve_forever()
