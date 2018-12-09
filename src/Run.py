#!/usr/bin/python3
import socket
from Initialize import joinRoom



def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(("PASS " + PASS + "\r\n").encode())
    s.send(("NICK " + IDENT + "\r\n").encode())
    s.send(("JOIN #" + CHANNEL + "\r\n").encode())
    return s


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())

# Gets username and message from the most recent post
def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message
