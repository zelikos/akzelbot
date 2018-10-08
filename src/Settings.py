import sys


def load_settings():
    settings = {}
    try:
        settings_file = open("../data/settings.txt", "r")
    except FileNotFoundError:
        print("Settings file not found.")
        sys.exit(0)
    else:
        for line in settings_file:
            line = line.split()
            settings[line[0]] = line[1]
    finally:
        settings_file.close()
    return settings


settings = load_settings()


HOST = "irc.twitch.tv"
PORT = 6667
PASS = settings["oauth"]
IDENT = settings["account"]
CHANNEL = settings["channel"]
