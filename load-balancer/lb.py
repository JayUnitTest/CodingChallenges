from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
from health_checks import HealthChecker
from itertools import cycle
import yaml

try:
    with open("servers.yaml", "r") as file:
        data = yaml.safe_load(file)
except FileNotFoundError:
    print(f"Error: servers file could not be found")
except Exception as e:
    print("Unexpected Error:", e)

HOST = "127.0.0.1"
PORT = 80
BACKEND_SERVERS = []

for server in data["Servers"]:
    host = server["host"]
    port = int(server["port"])
    BACKEND_SERVERS.append((host, port))

# each time a Get request is received, cycle is called to get the next backend server from the cycle. (round robin)
backend_cycle = cycle(BACKEND_SERVERS)

health_checker = HealthChecker(BACKEND_SERVERS)
health_checker.start()


class LoadBalancerHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        available_servers = [
            server for server, status in health_checker.backend_status.items() if status
        ]
        if not available_servers:
            self.send_error(503, "Service Unavailable")
            return

        # Selecting backend server and cycling through (round robin)
        backend_host, backend_port = next(backend_cycle)
        print(f"Received request from {self.client_address[0]}")
        for header in self.headers:
            print(f"{header}: {self.headers[header]}")

        # attempt to establish a connection to the backend. if successful it proxies the clients request to the backend server and
        # forwards the response back to the client
        try:
            client = http.client.HTTPConnection(backend_host, backend_port)
            client.request(self.command, self.path, headers=self.headers)
            response = client.getresponse()

            if response.status != 200:
                health_checker.backend_status[(backend_host, backend_port)] = False
                print(f"Server {backend_host}:{backend_port} is marked as unhealthy.")
            else:
                self.send_response(response.status, response.reason)
                for header in response.getheaders():
                    self.send_header(header[0], header[1])
                self.end_headers()
                self.wfile.write(response.read())
        except ConnectionRefusedError:
            # Connection refused, this will mark server as unhealthy
            health_checker.backend_status[(backend_host, backend_port)] = False
            print(
                f"Connection refused to server, server is closed: {backend_host}:{backend_port}"
            )


server = HTTPServer(("", PORT), LoadBalancerHTTP)
print(f"Server is now running on host: {HOST}, port: {PORT}")
server.serve_forever()
