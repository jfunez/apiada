import json
from random import choices
from http.server import SimpleHTTPRequestHandler

jokes_raw = open('potasio.json').read()
# jokes_raw = open('jokes.json').read()
jokes_dict = json.loads(jokes_raw)


class ApiHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # random joke:
        joke = choices(jokes_dict)
        # content = bytes(str(joke, "UTF-8"))
        content = json.dumps(joke).encode('utf-8')

        # send response
        self.wfile.write(content)
