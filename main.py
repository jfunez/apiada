#!/usr/bin/env python3
from http.server import HTTPServer
from server import ApiHandler

HOST_NAME = 'localhost'
PORT_NUMBER = 8000


if __name__ == '__main__':
    # criamos o servidor
    httpd = HTTPServer(
        (HOST_NAME, PORT_NUMBER),
        ApiHandler)

    # iniciamos o servidor
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    # finalizamos o servidor
    httpd.server_close()
