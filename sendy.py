#!/usr/bin/env python
from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
from SocketServer import TCPServer

def start_server(port):
    print "HTTP server listening on {0}".format(port)
    httpd = TCPServer(("", port), Handler)
    httpd.serve_forever()

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Start a tiny http server to share files')
    parser.add_argument('-p', dest='port', metavar='port', default=4200, type=int)
    parser.add_argument('-f', dest='file', metavar='file', nargs=1)
    args = parser.parse_args()
    if args.file:
        print "This mode is not yet supported"
    else:
        start_server(args.port)
