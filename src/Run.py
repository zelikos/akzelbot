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


# Gets username and message from the most recent post
def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message
