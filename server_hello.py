from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8001


class HelloHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


with socketserver.TCPServer(("", PORT), HelloHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
