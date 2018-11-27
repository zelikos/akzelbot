import json
import sys


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())


def load_config():
    try:
        config_file = open("../config/config.json")
    except FileNotFoundError:
        print("Config file not found.")
#        initial_setup()
    else:
        config = json.load(config_file)
    finally:
        config_file.close()
    return config


def save_config():
    with open('../config/config.json', 'w') as outfile:
        json.dump(config, outfile)


#def initial_setup():
config = load_config()


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
    print(config["login"]["account"] + " has joined " + CHANNEL)


def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True


HOST = "irc.twitch.tv"
PORT = 6667
PASS = config["login"]["oauth"]
IDENT = config["login"]["account"]
CHANNEL = config["login"]["channel"]
