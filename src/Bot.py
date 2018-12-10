# Copyright (c) 2018 Patrick Csikos (https://github.com/Akzel94)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA


import socket
import sys


class Bot:
    def __init__(self, username, oauth, channel, lists, HOST = "irc.twitch.tv", PORT = 6667):
        self.username = username
        self.oauth = oauth
        self.channel = channel
        self.HOST = HOST
        self.PORT = PORT
        self.mods = lists["mods"]
        self.puns = lists["puns"]
        self.quotes = lists["quotes"]
        self.local_commands = lists["commands"]
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


    def joinRoom(self, s):
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
        print(IDENT + " has joined " + CHANNEL)


    def loadingComplete(self, line):
        if("End of /NAMES list" in line):
            return False
        else:
            return True


    def sendMessage(self, s, message):
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
        s.send((messageTemp + "\r\n").encode())
