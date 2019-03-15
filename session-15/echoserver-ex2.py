import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8000


def read_contents(page):
    with open('{}.html'.format(page), 'r') as html_file:
        contents = html_file.read()
    return contents


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        # msg = self.requestline.partition('msg=')[2].partition(' ')[0]

        if self.path == '/':
            contents = read_contents("form-ex2")

        elif 'msg' in self.path:
            contents = read_contents("echo")
            message = self.path[self.path.index('=')+1:]
            if 'chk=on' in message:
                message = message[:message.index('&')]
                contents = contents.format(message.upper())
            else:
                contents = contents.format(message)

        else:
            contents = read_contents('error')

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the body of the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")