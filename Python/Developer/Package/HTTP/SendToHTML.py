#!/usr/bin/python3.13
from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Define the HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Dynamic HTML</title>
        </head>
        <body>
	    <h1>Hello From {host}:{port}</h1>
            <h2>Welcome to My Python HTTP Server</h2>
            <p>This is a dynamically generated HTML page.</p>
        </body>
        </html>
        """
        # Send response status code
        self.send_response(200)
        # Set the response headers
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        # Write the HTML content to the response
        self.wfile.write(html_content.encode("utf-8"))

# Server setup
server = HTTPServer((host, port), MyHandler)
print(f"Serving on http://{host}:{port}")
server.serve_forever()
