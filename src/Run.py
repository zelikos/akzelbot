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


import time
from Bot import Bot
from Initialize import save_lists, config, lists


account = config["account"]
oauth = config["oauth"]
channel = config["channel"]

akzelbot = Bot(account, oauth, channel, lists)


s = akzelbot.getSocket()
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
        if first_word in akzelbot.local_commands:
            akzelbot.run_command(first_word)

        if "!pun" == first_word:
            akzelbot.get_pun(first_word)
        if "!quote" == first_word:
            akzelbot.get_quote(first_word)
        if "!addpun" == first_word:
            akzelbot.add_pun(message)
            save_lists()
        if "!addquote" == first_word:
            akzelbot.add_quote(message)
            save_lists()

        if "!startraffle" == first_word:
            if user == akzelbot.channel or user in akzelbot.mods:
                akzelbot.start_raffle()

        if "!raffle" == first_word:
            if akzelbot.raffle == True:
                if user not in akzelbot.raffle_entries:
                    akzelbot.enter_raffle(user)

        if "!winner" == first_word:
            if akzelbot.raffle == True:
                akzelbot.raffle_winner()

        if "!closeraffle" == first_word:
            if user == akzelbot.channel or user in akzelbot.mods"
                akzelbot.close_raffle()

        if "!addcommand" == first_word:
            if user == akzelbot.channel or user in akzelbot.mods:
                akzelbot.add_command(message)
                save_lists()
            else:
                akzelbot.sendMessage(akzelbot.s, "Only moderators can add commands.")
        if "!command" == first_word:
            if user == akzelbot.channel or user in akzelbot.mods:
                akzelbot.add_command(message)
                save_lists()
            else:
                akzelbot.sendMessage(akzelbot.s, "Only moderators can modify commands.")
        if "!delcommand" == first_word:
            if user == akzelbot.channel:
                akzelbot.del_command(message)
                save_lists()
            else:
                akzelbot.sendMessage(akzelbot.s, "Only the channel owner can remove commands.")

        if "!addmod" == first_word:
            if user == akzelbot.channel:
                akzelbot.add_mod(message)
                save_lists()
            else:
                akzelbot.sendMessage(akzelbot.s, "Only the channel owner can add mods.")
        if "!delmod" == first_word:
            if user == akzelbot.channel:
                akzelbot.del_mod(message)
                save_lists()
            else:
                akzelbot.sendMessage(akzelbot.s, "Only the channel owner can remove mods.")

        if "!quit" == first_word:
            if user == akzelbot.channel:
                akzelbot.sendMessage(akzelbot.s, "Exiting.")
                akzelbot.close_bot()

        if "!kill" == first_word:
            if user != akzelbot.channel and user in akzelbot.mods:
                akzelbot.sendMessage(akzelbot.s, "You cannot kill that which is immortal.")
            elif user == akzelbot.channel:
                akzelbot.sendMessage(akzelbot.s, "AAAGGGHHH!")
                akzelbot.close_bot()

    time.sleep(0.7)
