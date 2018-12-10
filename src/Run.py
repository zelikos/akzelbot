#!/usr/bin/python3

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
import time
from Bot import Bot
from Config import save_lists, config, lists


account = config["login"]["account"]
oauth = config["login"]["oauth"]
channel = config["login"]["channel"]

akzelbot = Bot(account, oauth, channel, lists)


def openSocket():
    s = socket.socket()
    s.connect((akzelbot.HOST, akzelbot.PORT))
    s.send(("PASS " + akzelbot.oauth + "\r\n").encode())
    s.send(("NICK " + akzelbot.username + "\r\n").encode())
    s.send(("JOIN #" + akzelbot.channel + "\r\n").encode())
    return s


s = openSocket()
akzelbot.joinRoom(s)
readbuffer = ""


# Gets username and message from the most recent post
def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message


def console(line):
    # gets if it is a user or twitch server
    if "PRIVMSG" in line:
        return False
    else:
        return True


while True:
    try:
        readbuffer = s.recv(1024)
        readbuffer = readbuffer.decode()
        temp = readbuffer.split("\n")
        readbuffer = readbuffer.encode()
        readbuffer = temp.pop()
    except:
        temp = ""
    for line in temp:
        if line == "":
            break
        # to prevent the bot being timed out
        if "PING" in line and console(line):
            msgg = "PONG :tmi.twitch.tv\r\n".encode()
            s.send(msgg)
            print(msgg)
            break
        # get user
        user = getUser(line)
        # get message sent by user
        message = getMessage(line)
        print(user + " : " + message)
        PMSG = "/w" + user + " "


        # COMMANDS

        # Takes first word of a user's message
        first_word = message.split()[0]

        if first_word in commands:
            sendMessage(s, str(commands[first_word]))
        if "!pun" == first_word:
            try:
                sendMessage(s, str(random.choice(puns)))
            except IndexError:
                sendMessage(s, "Sadly, I have no puns to choose from.")
                time.sleep(0.7)
                sendMessage(s, "Try adding one with !addpun")
        if "!quote" == first_word:
            try:
                sendMessage(s, str(random.choice(quotes)))
            except IndexError:
                sendMessage(s, "Sadly, I have no quotes to choose from.")
                time.sleep(0.7)
                sendMessage(s, "Try adding one with !addquote")
        if "!addpun" == first_word:
            if user in mods or user == CHANNEL:
                add_item(message, "pun")
            elif not user in mods:
                sendMessage(s, "Only moderators can apPUNd the pun list.")
                time.sleep(0.7)
                sendMessage(s, "Sorry, that was terrible.")
        if "!addquote" == first_word:
            if user in mods or user == CHANNEL:
                add_item(message, "quote")
            elif not user in mods:
                sendMessage(s, "Only moderators can append the quote list.")
        if "!addcommand" == first_word:
            if user == CHANNEL or user in mods:
                add_item(message, "command")
            else:
                sendMessage("Only moderators can add commands.")
        if "!delcommand" == first_word:
            if user == CHANNEL:
                del_command(message)
            else:
                sendMessage("Only the channel owner can remove commands.")
        if "!addmod" == first_word:
            if user == CHANNEL:
                add_item(message, "mod")
            else:
                sendMessage(s, "Only the channel owner can add mods.")
        if "!delmod" == first_word:
            if user == CHANNEL:
                del_mod(message)
            else:
                sendMessage(s, "Only the channel owner can remove mods.")

        if "!quit" == first_word:
            if user == CHANNEL:
                sendMessage(s, "Exiting.")
                time.sleep(0.7)
                sys.exit(0)

        if "!kill" == first_word:
            if user != CHANNEL and user in mods:
                sendMessage(s, "You cannot kill that which is immortal.")
            elif user == CHANNEL:
                sendMessage(s, "AAAGGGHHH!")
                time.sleep(0.7)
                sys.exit(0)

    time.sleep(0.7)
