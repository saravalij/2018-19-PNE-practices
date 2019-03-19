import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')

        list_resource = self.path.split('?')
        resource = list_resource[0]

        if resource == "/":
            f = open("index.html", 'r')
            code = 200
            contents = f.read()

            content_type = 'text/html'

        elif resource == "/listusers":
            f = open("ex-1.json", 'r')
            code = 200
            contents = f.read()
            content_type = 'application/json'
        else:
            f = open("error.html", 'r')
            code = 404
            contents = f.read()
            content_type = 'text/html'

        self.send_response(code)  # -- Status line: OK!

        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
