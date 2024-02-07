import threading
import time
import http.client


class HealthChecker(threading.Thread):
    def __init__(self, backend_servers):
        super().__init__()
        self.backend_status = {server: True for server in backend_servers}

    def run(self):
        while True:
            for server in self.backend_status:
                host, port = server
                try:
                    conn = http.client.HTTPConnection(host, port)
                    conn.request("GET", "/")
                    response = conn.getresponse()
                    if response.status == 200:
                        self.backend_status[server] = True
                        print(f"Server {server} is now healthy.")
                    else:
                        self.backend_status[server] = False
                        print(f"Server {server} is now unhealthy.")
                except Exception as e:
                    self.backend_status[server] = False
                    print("Error Occurred, server is closed", e)
            time.sleep(10)
            print("Server(s) state:", self.backend_status)
