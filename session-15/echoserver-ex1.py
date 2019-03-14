import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8001


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        msg = self.requestline.partition('msg=')[2].partition(' ')[0]

        if self.path == '/':
            f = open("form-ex1.html", 'r')
            contents = f.read()
            f.close()

        elif msg in self.path:
            file = open('echo.html', 'w')
            file.write('''
            <!DOCTYPE html>
                <html lang="en" dir="ltr">
                    <head>
                        <meta charset="utf-8">
                        <title>eco?</title>
                    </head>
                    <body style="background-color: pink;">
                        <h1>Eco del mensaje recibido</h1>
                        <p>{}</p>
                        <a href="/">Back to the form</a>
                    </body>
            </html>'''.format(msg))
            file.close()
            file = open('echo.html', 'r')
            contents = file.read()
            file.close()

        else:
            f = open("error.html", 'r')
            contents = f.read()
            f.close()

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
