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


import random
import socket
import sys
import time


class Bot:
    def __init__(self, username, oauth, channel, lists, HOST = "irc.twitch.tv", PORT = 6667):
        self.username = username
        self.oauth = oauth
        self.channel = channel
        self.HOST = HOST
        self.PORT = PORT
        self.s = self.openSocket()
        self.mods = lists["mods"]
        self.puns = lists["puns"]
        self.quotes = lists["quotes"]
        self.local_commands = lists["commands"]
        # self.bot_commands = {'!pun': get_pun,
        #                      '!quote': get_quote,
        #                      '!addpun': add_pun,
        #                      '!addquote': add_quote,
        #                      '!addcommand': add_command,
        #                      '!delcommand': del_command,
        #                      '!addmod': add_mod,
        #                      '!delmod': del_mod,
        #                      '!quit': close_bot,
        #                      '!kill': kill_bot}


    def run_command(self, parameter):
        self.sendMessage(self.s, self.local_commands[parameter])


    def new_item(self, input):
        new_item = []
        try:
            new_item = input.split()
            new_item = (" ").join(new_item[1:])
        except IndexError:
            pass
        else:
            return new_item


    def get_pun(self, input):
        try:
            self.sendMessage(self.s, str(random.choice(self.puns)))
        except IndexError:
            self.sendMessage(self.s, "No puns available. Try adding one with !addpun")


    def get_quote(self, input):
        try:
            self.sendMessage(self.s, str(random.choice(self.quotes)))
        except IndexError:
            self.sendMessage(self.s, "No quotes available. Try adding one with !addquote")


    def add_pun(self, input):
        if len(self.new_item(input)) >= 1:
            self.puns.append(self.new_item(input))
            self.sendMessage(self.s, "Pun added.")


    def add_quote(self, input):
        if len(self.new_item(input)) >= 1:
            self.quotes.append(self.new_item(input))
            self.sendMessage(self.s, "Quote added.")


    def add_command(self, input):
        new_command = input.split()
        if len(new_command) <= 2:
            self.sendMessage(self.s, "Syntax: '!command !newcommand command-text'")
        elif new_command[1][0] != "!":
            self.sendMessage(self.s, "Keyword must be prefixed with '!'.")
        else:
            self.local_commands[new_command[1]] = (' ').join(new_command[2:])
            self.sendMessage(self.s, "Command added.")


    def del_command(self, input):
        dead_command = input.split()[1]
        if dead_command in self.local_commands.keys():
            del self.local_commands[dead_command]
            self.sendMessage(self.s, "Command removed.")
        else:
            self.sendMessage(self.s, "No command found.")


    def add_mod(self, input):
        if self.new_item(input) == self.channel:
            self.sendMessage(self.s, "...Really?")
        elif self.new_item(input) in self.mods:
            self.sendMessage(self.s, "User is already a moderator.")
        else:
            self.mods.append(new_item(input))
            self.sendMessage(self.s, "Moderator added.")


    def del_mod(self, input):
        if self.new_item(input) == self.channel:
            self.sendMessage(self.s, "Not possible.")
        elif self.new_item(input) in self.mods:
            self.mods.remove(new_item(input))
            self.sendMessage(self.s, "Moderator removed.")


    def close_bot(self):
        self.sendMessage(self.s, "Exiting.")
        time.sleep(0.7)
        sys.exit(0)


    def kill_bot(self):
        self.sendMessage(self.s, "AAAGGGHHH!")
        time.sleep(0.7)
        sys.exit(0)


    def openSocket(self):
        s = socket.socket()
        s.connect((self.HOST, self.PORT))
        s.send(("PASS " + self.oauth + "\r\n").encode())
        s.send(("NICK " + self.username + "\r\n").encode())
        s.send(("JOIN #" + self.channel + "\r\n").encode())
        return s


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
                Loading = self.loadingComplete(line)
        self.sendMessage(self.s, "Successfully joined chat.")
        print(self.username + " has joined " + self.channel)


    def loadingComplete(self, line):
        if("End of /NAMES list" in line):
            return False
        else:
            return True


    def sendMessage(self, s, message):
        messageTemp = "PRIVMSG #" + self.channel + " :" + message
        s.send((messageTemp + "\r\n").encode())
