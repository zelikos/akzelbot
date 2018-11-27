import socket
from Initialize import HOST, PORT, PASS, IDENT, CHANNEL


def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(("PASS " + PASS + "\r\n").encode())
    s.send(("NICK " + IDENT + "\r\n").encode())
    s.send(("JOIN #" + CHANNEL + "\r\n").encode())
    return s
