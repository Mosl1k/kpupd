from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import  subprocess, sys

subprocess.Popen(['kill', '-9', 'run.py']) 
subprocess.Popen(['python3', 'run.py'])

if len (sys.argv) > 1:
    #print(sys.argv[1])
    port = int(sys.argv[1])      

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # определяем метод `do_GET` 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    # определяем метод `do_POST` 
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
httpd.serve_forever()



