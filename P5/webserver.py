import http.server
import socketserver
import termcolor

PORT = 8008

def read_contents(page):
    with open('{}.html'.format(page), 'r') as html_file:
        contents = html_file.read()
    return contents

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')

        print('Request line:' + self.requestline)
        print('Cmd:' + self.command)
        print('Path:' + self.path)

        if self.path == '/':
            request = 'index'
        elif self.path == '/pink':
            request = 'pink'
        elif self.path == '/blue':
            request = 'blue'
        else:
            request = 'error'

        contents = read_contents(request)

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
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