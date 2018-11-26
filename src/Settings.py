# Copyright (c) 2018 Patrick Csikos (https://github.com/Akzel94)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA


import sys


def load_settings():
    settings = {}
    try:
        settings_file = open("../config/settings.txt", "r")
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
