class Bot:
    def __init__(self, username, oauth, channel, HOST = "irc.twitch.tv", PORT = 6667):
        self.username = username
        self.oauth = oauth
        self.channel = channel
        self.HOST = HOST
        self.PORT = PORT

    bot_commands = {}

    def run_command(parameter):
        
