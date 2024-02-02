from http.server import HTTPServer, BaseHTTPRequestHandler


HOST = '127.0.0.1'
PORT = 8000


class HTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        print(f"Received request from {self.client_address[0]}")
        print(self.requestline)
        for header in self.headers:
            print(f"{header}: {self.headers[header]}")
        print()

        self.send_response(200, "Replied with a hello message")
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        response_body = "Hello from Backend Server"
        self.wfile.write(response_body.encode("utf-8"))

server = HTTPServer((HOST, PORT), HTTP)
print(f"Server is now running on host: {HOST}, port: {PORT}")
server.serve_forever()
server.server_close()