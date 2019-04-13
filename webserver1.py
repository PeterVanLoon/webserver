from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver



class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "Hello!" ###<html><body></body></html>
            self.wfile.write(message.encode('utf-8'))
            print (message)
            return
        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = ""
            message += "&#161Hola? <a href = '/hello' >Back to Hello</a>" ###<html><body></body></html>
            self.wfile.write(message.encode('utf-8'))
            print (message)
            return

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)
	def do_POST(self):
		try:
			self,send_response(301)
			self.end_headers()

			ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
			if ctype == 'multipart/form data':
				fields =cgi.parse_multipart(self, rfile, pdict)
				messagecontent = fields.get('message')

			output = ""
			output = ""
			pass
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass

def main():
    try:
        port = 8000
        server = HTTPServer(('', port), WebServerHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()