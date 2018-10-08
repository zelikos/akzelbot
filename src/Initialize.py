from Socket import sendMessage
from Settings import CHANNEL


def joinRoom(s):
    readbuffer_join = "".encode()
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        temp = readbuffer_join.split("\n")
        readbuffer_join = readbuffer_join.encode()
        readbuffer_join = temp.pop()
        for line in temp:
            Loading = loadingComplete(line)
    sendMessage(s, "Successfully joined chat.")
    print("akzelbot has joined " + CHANNEL)


def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
