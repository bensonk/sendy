#!/usr/bin/env python
from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
from SocketServer import TCPServer
from sys import argv

def start_server(port):
    httpd = TCPServer(("", port), Handler)
    httpd.serve_forever()

def usage():
    print "usage: sendy.py <port>"

if __name__ == "__main__":
    try:
        port = int(argv[1])
        start_server(port)
    except:
        usage()
