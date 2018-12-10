class Bot:
    def __init__(self, username, oauth, channel, lists, HOST = "irc.twitch.tv", PORT = 6667):
        self.username = username
        self.oauth = oauth
        self.channel = channel
        self.HOST = HOST
        self.PORT = PORT
        self.local_commands = lists
        self.bot_commands = {'!pun': get_pun,
                             '!quote': get_quote,
                             '!addpun': add_pun,
                             '!addquote': add_quote,
                             '!addcommand': add_command,
                             '!delcommand': del_command,
                             '!addmod': add_mod,
                             '!delmod': del_mod,
                             '!quit': close_bot,
                             '!kill': kill_bot}


    def run_command(self, parameter, input):
        if parameter in self.bot_commands:
            self.bot_commands[parameter](input)
        elif parameter in self.local_commands:
            pass


    def new_item(self, input):
        new_item = []
        try:
            new_item = input.split()
            new_item = (" ").join(new_item[1:])
        except IndexError:
            sendMessage(s, '/w ' + user + ' Syntax: !command argument')
        else:
            return new_item


    def get_pun(self, input):
        pass


    def get_quote(self, input):
        pass


    def add_pun(self, input):
        pass


    def add_quote(self, input):
        pass


    def add_command(self, input):
        new_command = input.split()
        if len(new_command) <= 2:
            sendMessage(s, "Syntax: '!command !newcommand command-text'")
        elif new_command[1][0] != "!":
            sendMessage(s, "Keyword must be prefixed with '!'.")
        else:
            commands[new_command[1]] = (' ').join(new_command[2:])
            sendMessage(s, "Command added.")


    def del_command(self, input):
        dead_command = input.split()[1]
        if dead_command in commands.keys():
            del commands[dead_command]
            sendMessage(s, "Command removed.")
        else:
            sendMessage(s, "No command found.")


    def add_mod(self, input):
        if new_item(input) == CHANNEL:
            sendMessage(s, "...Dood, really?")
        elif new_item(input) in mods:
            sendMessage(s, "User is already a moderator.")
        else:
            mods.append(new_item(input))
            sendMessage(s, "Moderator added.")


    def del_mod(self, input):
        if new_item(input) == CHANNEL:
            sendMessage(s, "Not possible.")
        elif new_item(input) in mods:
            mods.remove(new_item(input))
            sendMessage(s, "Moderator removed.")




    # def add_item(input, item_type):
    #     if len(new_item(input)) >= 1:
    #         if item_type == "pun":
    #             puns.append(new_item(input))
    #             sendMessage(s, "Pun added.")
    #         elif item_type == "quote":
    #             quotes.append(new_item(input))
    #             sendMessage(s, "Quote added.")
    #         elif item_type == "mod":
    #             add_mod(input)
    #             save_config()
    #         elif item_type == "command":
    #             add_command(input)
    #             save_config()
