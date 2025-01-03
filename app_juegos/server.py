import http.server
import socketserver
import os

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/about':
            self.path = 'templates/about.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Sirviendo en el puerto {PORT}")
httpd.serve_forever()
