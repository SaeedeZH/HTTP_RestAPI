from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if re.search('/tasks/*',self.path):
            record_id = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps({'tasks': tasks[int(record_id)]}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        if self.path == '/tasks':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_task = json.loads(post_data.decode('utf-8'))

            if 'title' in new_task:
                new_task['id'] = len(tasks) + 1
                new_task['done'] = False
                tasks.append(new_task)

                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'task': new_task}).encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Title is required"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

if __name__ == '__main__':
    tasks = [
        {'id': 1, 'title': 'Task 1', 'done': False},
        {'id': 2, 'title': 'Task 2', 'done': False}
    ]

    server_address = ('', 5000)  # '' means localhost with 127.0.0.1 ip, port 
    httpd = HTTPServer(server_address, SimpleHandler)
    print('Server running on port 5000...')
    httpd.serve_forever() # this command must be the last insruction for this http server
