from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Server started at http://{host}:{port}")

server.serve_forever()
