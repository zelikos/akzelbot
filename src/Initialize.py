import json
import sys


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())


def load_config():
    try:
        config_file = open("../config.json")
    except FileNotFoundError:
        print("Config file not found.")
        print("Starting initial setup...")
        return initial_setup()
    else:
        config = json.load(config_file)
        config_file.close()
    return config


def save_config():
    with open('../config.json', 'w') as outfile:
        json.dump(config, outfile)


def initial_setup():
    bot_account = input("Enter bot's Twitch account name: ")
    print("Next, generate an oauth token (i.e. from https://twitchapps.com/tmi/) for the bot's account.")
    bot_oauth = input("Enter it here: ")
    user_channel = input("Finally, enter the name of the channel that the bot will monitor: ")
    print("Creating config.json...")
    config = {"login": {"account": bot_account,
                        "oauth": bot_oauth,
                        "channel": user_channel},
            "mods": [],
            "puns": [],
            "quotes": [],
            "commands": {}}
    return config


config = load_config()
save_config()


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
