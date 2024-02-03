from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
from itertools import cycle
import yaml

try:
    with open('servers.yaml', 'r') as file:
        data = yaml.safe_load(file)
except FileNotFoundError:
    print(f"Error: servers file could not be found")
except Exception as e:
    print("Unexpected Error:", e )


HOST = '127.0.0.1'
PORT = 80
BACKEND_SERVERS = [(server['host'], int(server['port'])) for server in data['Servers']]
#each time a Get request is received, cycle is called to get the next backend server from the cycle. 
backend_cycle = cycle(BACKEND_SERVERS)


class LoadBalancerHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        backend_host, backend_port = next(backend_cycle)
        
        print(f"Received request from {self.client_address[0]}")
        print(self.requestline)
        for header in self.headers:
            print(f"{header}: {self.headers[header]}")
        print()
                
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
        self.wfile.flush()

server = HTTPServer(('', PORT), LoadBalancerHTTP)
print(f"Server is now running on host: {HOST}, port: {PORT}")
server.serve_forever()