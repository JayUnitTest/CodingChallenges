from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client


HOST = '127.0.0.1'
PORT = 80


class LoadBalancerHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        print(f"Received request from {self.client_address[0]}")
        print(self.requestline)
        for header in self.headers:
            print(f"{header}: {self.headers[header]}")
        print()
                
        backend_host = '127.0.0.1'
        backend_port = 8000
        client = http.client.HTTPConnection(backend_host, backend_port)
        client.request(self.command, self.path, headers=self.headers)
        response = client.getresponse()
        
        self.send_response(200, "OK")
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        print(f"Response from server: {response.status} \n {response.reason}")
        for header in response.getheaders():
            print(f"{header[0]}: {header[1]}")
        print()
        self.wfile.write(response.read())

server = HTTPServer((HOST, PORT), LoadBalancerHTTP)
print(f"Server is now running on host: {HOST}, port: {PORT}")
server.serve_forever()
server.server_close()