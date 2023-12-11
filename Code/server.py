import os
import mimetypes
import socket
import ssl
import subprocess
import sys
import datetime
from parser_http import parse_request

class Server:
    def __init__(self):
        if len(sys.argv) < 3 or len(sys.argv) == 4 or len(sys.argv) > 5:
            print("Usage: python server.py <host> <port>")
            sys.exit(1)

        self.host = sys.argv[1]
        self.port = int(sys.argv[2])

        self.status_terms = {
            200: "OK",
            201: "Created",
            400: "Bad Request",
            403: "Forbidden",
            404: "Not Found",
            411: "Length Required",
            500: "Welcome to my WebPage(SI5823)",
            501: "Not Implemented",
            505: "HTTP Version Not Supported"
        }

        if len(sys.argv) == 5:
            self.cert_file = sys.argv[3]
            self.key_file = sys.argv[4]
            self.use_https = True
        elif len(sys.argv) == 3:
            self.cert_file = None
            self.key_file = None
            self.use_https = False
        else:
            print("Usage: python server.py <host> <port> <cert_file> <key_file>")
            sys.exit(1)
        
        self.GET_ENV_VARS = {
            "QUERY_STRING": "",
            "SCRIPT_NAME": "",
            "SCRIPT_FILENAME": "",
            "REQUEST_METHOD": "GET",
            "REDIRECT_STATUS": '0',
            "REMOTE_HOST": ""
        }

        self.POST_ENV_VARS = {
            "QUERY_STRING": "",
            "SCRIPT_NAME": "",
            "SCRIPT_FILENAME": "",
            "REQUEST_METHOD": "POST",
            "GATEWAY_INTERFACE": "CGI/1.1",
            "REDIRECT_STATUS": '1',
            "CONTENT_TYPE": 'application/x-www-form-urlencoded',
            "CONTENT_LENGTH": '0',
            "REMOTE_HOST": ""
        }

        self.start()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))

        if self.use_https:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(self.cert_file, self.key_file)
            server_socket = context.wrap_socket(server_socket, server_side=True)
            print(f"[info] HTTPS server started on {self.host}:{self.port}...\n")
        else:
            print(f"[info] HTTP Server started on {self.host}:{self.port}...\n")

        server_socket.listen(5)



        while True:
            conn, addr = server_socket.accept()
            print(f"[info] New {'HTTPS' if self.use_https else 'HTTP'} connection from {addr}\n")
            try:
                request_data = conn.recv(1024).decode('iso-8859-1')

                if not request_data:
                    continue
                parsed_request = parse_request(request_data)

                if len(parsed_request) == 1:
                    response_data = self.build_error_response(parsed_request[0])
                    conn.sendall(response_data)
                    conn.close()
                    continue
                [method, path, headers, body] = parsed_request if len(parsed_request) == 4 else parsed_request + (None, None, None)


                # log the request
                self.log_request(request_data.splitlines()[0])
                requested_path = os.path.join(os.getcwd(), path.lstrip('/'))

                # Check if the requested file exists
                if not os.path.isfile(requested_path):
                    response_data = self.build_error_response(404)
                    conn.sendall(response_data)
                    conn.close()
                    continue

                # Handle GET request
                if method == 'GET':
                    response_data = self.build_get_response(requested_path)
                    conn.sendall(response_data)
                    conn.close()
                # Handle POST request
                elif method == 'POST':
                    if 'Content-Length' not in headers:
                        response_data = self.build_error_response(411)
                        conn.sendall(response_data)
                        conn.close()
                        continue
                    response_data = self.build_post_response(requested_path, headers, body)
                    conn.sendall(response_data)
                    conn.close()
                # Handle PUT and DELETE requests
                elif method == 'PUT':
                    response_data = self.build_put_response(requested_path, headers, body)
                    conn.sendall(response_data)
                    conn.close()
                # Handle DELETE request
                elif method == 'DELETE':
                    response_data = self.build_delete_response(requested_path)
                    conn.sendall(response_data)
                    conn.close()
                # Handle HEAD request
                elif method == 'HEAD':
                    response_data = self.build_head_response(requested_path)
                    conn.sendall(response_data)
                    conn.close()
                # Handle CONNECT request
                elif method == 'CONNECT':
                    response_data = self.build_connect_response(requested_path)
                    conn.sendall(response_data)
                    conn.close()
                else:
                    response_data = self.build_error_response(400)
                    conn.sendall(response_data)
                    conn.close()
            except Exception as e:
                print(f"[error] {e}")
                response_data = self.build_error_response(500)
                conn.sendall(response_data)
                conn.close()

    def log_request(self, request):
        now = datetime.datetime.now()
        print(f"[{now}] {request}")

    def build_get_response(self, path):
        file_extension = os.path.splitext(path)[1]
        if file_extension == '.php':
            process = subprocess.Popen(['php', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            content, stderr_data = process.communicate()

            if stderr_data:
                print(f"[error] {stderr_data.decode('iso-8859-1')}")
            content_type = 'text/html'
        else:
            with open(path, 'rb') as f:
                content = f.read()
                content_type = mimetypes.guess_type(path)[0] or 'application/octet-stream'

        if content_type is None:
            content_type = 'application/octet-stream'

        response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n"
        return response.encode('iso-8859-1') + content

    def build_post_response(self, path, headers, body):
        file_extension = os.path.splitext(path)[1]
        if file_extension == '.php':
            env_vars = self.POST_ENV_VARS.copy()
            env_vars['REQUEST_METHOD'] = 'POST'
            env_vars['CONTENT_LENGTH'] = headers['Content-Length']
            env_vars['CONTENT_TYPE'] = headers.get('Content-Type', 'application/x-www-form-urlencoded')
            env_vars['SCRIPT_FILENAME'] = path
            env_vars['SCRIPT_NAME'] = os.path.basename(path)
            env_vars['POST_DATA'] = body

        # Merge the current environment variables with the custom variables
            merged_env_vars = os.environ.copy()
            merged_env_vars.update(env_vars)

            process = subprocess.Popen(['php', path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=merged_env_vars)
            content, stderr_data = process.communicate(input=body.encode('iso-8859-1'))

            if stderr_data:
                print(f"[debug] post.php stderr_data: {stderr_data.decode('iso-8859-1')}")
            content_type = 'text/html'
        else:
            with open(path, 'rb') as f:
                content = f.read()
                content_type = mimetypes.guess_type(path)[0] or 'application/octet-stream'

        if content_type is None:
            content_type = 'application/octet-stream'

        response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n"
        return response.encode('iso-8859-1') + content
    
    def build_error_response(self, status_code):
        status_text = self.status_terms.get(status_code, 'Unknown Error')
        content = f"<h1>{status_code} {status_text}</h1>".encode('iso-8859-1')
        content_type = 'text/html'
        response = f"HTTP/1.1 {status_code} {status_text}\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n"
        return response.encode('iso-8859-1') + content
    
    def log_request(self, request):
        now = datetime.datetime.now()
        log_entry = f"[{now}] {request}"
        print(log_entry)
        with open('server.log', 'a') as log_file:
            log_file.write(log_entry + "\n")


if __name__ == "__main__":
    server = Server()
                   
