import socket
import urlparse

urls = ['http://www.example.com', 'https://www.example.com']

for u in urls:
    try:
        p_url = urlparse.urlparse(u)
        print socket.getservbyname(p_url.scheme)
    except socket.error, msg:
        print '%15s : ERROR %s' % (u, msg)

