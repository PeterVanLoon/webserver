<<<<<<< HEAD
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                print ("This is before I print out restaurants") # My debug attempt
                print (restaurants) 
                print ("this is after") # My debug attempt
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "Is this working?"       # My debug attempt         
                output += "<html><body>"
                print ("one")  # My debug attempt
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br></br></br>"
                output += "It does seem to work"   # My debug attempt
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return            

            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>&#161Hola! <a href = '/hello' >Back to Hello</a></body></html>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(303)
            self.send_header('Content-type', 'text/html')
            print ("one")  # My debug attempt
            self.end_headers()
            print ("two") # My debug attempt
            ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            print ("three") # My debug attempt
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':    # Compare this line with your code - form data -> form-data
                fields = cgi.parse_multipart(self.rfile, pdict)    # Compare this line with your code - self, rfile -> self.rfile
                messagecontent = fields.get('message')
            print ("four") # My debug attempt
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this you fools?:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
            output += "</body></html>"
            self.wfile.write(output.encode())
            print (output)
        except:
            pass

def main():
    try:
        port = 8000
        server = HTTPServer(('', port), webserverHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
||||||| merged common ancestors
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi



class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"###<html><body></body></html>
                self.wfile.write(output.encode())
                print (output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':    # Compare this line with your code - form data -> form-data
                fields = cgi.parse_multipart(self.rfile, pdict)    # Compare this line with your code - self, rfile -> self.rfile
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this you fools?:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0].decode()
            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
            output += "</body></html>"
            self.wfile.write(output.encode())
            print (output)
        except:
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
=======
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                print ("This is before I print out restaurants") # My debug attempt
                print (restaurants) 
                print ("this is after") # My debug attempt
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "Is this working?"       # My debug attempt         
                output += "<html><body>"
                print ("one")  # My debug attempt
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br></br></br>"
                output += "It does seem to work"   # My debug attempt
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return            

            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>&#161Hola! <a href = '/hello' >Back to Hello</a></body></html>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(303)
            self.send_header('Content-type', 'text/html')
            print ("one")  # My debug attempt
            self.end_headers()
            print ("two") # My debug attempt
            ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            print ("three") # My debug attempt
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':    # Compare this line with your code - form data -> form-data
                fields = cgi.parse_multipart(self.rfile, pdict)    # Compare this line with your code - self, rfile -> self.rfile
                messagecontent = fields.get('message')
            print ("four") # My debug attempt
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this you fools?:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
            output += "</body></html>"
            self.wfile.write(output.encode())
            print (output)
        except:
            pass

def main():
    try:
        port = 8000
        server = HTTPServer(('', port), webserverHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
>>>>>>> f462a3c8a786c62e5316f61875926012a2dc906b
    main()