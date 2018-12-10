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


import json


def load_config():
    try:
        config_file = open('../data/config.json')
    except FileNotFoundError:
        print("Config file not found.")
        print("Starting initial setup...")
        return initial_setup()
    else:
        config = json.load(config_file)
        config_file.close()
    return config


def load_lists():
    try:
        lists_file = open('../data/lists.json')
    except FileNotFoundError:
        lists = ("mods": [], "puns": [], "quotes": [], "commands": {})
    else:
        lists = json.load(lists_file)
        lists_file.close()
    return lists


def save_config():
    with open('../data/config.json', 'w') as outfile:
        json.dump(config, outfile)
    outfile.close()


def save_lists():
    with open('../data/lists.json', 'w') as outfile:
        json.dump(lists, outfile)
    outfile.close()


def initial_setup():
    bot_account = input("Enter bot's Twitch account name: ")
    print("Next, generate an oauth token (i.e. from https://twitchapps.com/tmi/) for the bot's account.")
    bot_oauth = input("Enter it here: ")
    user_channel = input("Finally, enter the name of the channel that the bot will monitor: ")
    print("Creating config.json...")
    config = {"account": bot_account, "oauth": bot_oauth, "channel": user_channel}
    return config


config = load_config()
lists = load_lists()
save_config()
save_lists()
