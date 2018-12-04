# AkzelBot


## Setup:

- Open terminal, go to `src` directory
- Run `python3 Main.py`
- Follow steps in Initial Setup


## Built-in commands:

These commands are those built-in to the code, that perform a specific function. Other commands that just have AkzelBot send a specific message to chat are stored in the `config.json` file. All commands are accessed through Twitch chat.
- `!pun` and `!quote`: return a random pun or quote from the respective lists stored in `config.json`
- `!addpun` and `!addquote`: add a pun or quote to the respective lists in `config.json`
    - Example: !addpun This is a pun
    - Example2: !addquote "This is a quote." Akzel, 2018.
    - Note: actual formatting of the pun or quote isn't necessary, you just need **something** after the respective command.
- `!addcommand` and `!delcommand`: add and delete non-built-in commands
    - Example1: !addcommand !potato What if I told you... Potato?
    - Example2: !delcommand !potato
- `!addmod` and `!delmod`: add and remove moderators
    - Example1: !addmod akzel94
    - Example2: !delmod akzel94
    - Note: Currently, AkzelBot uses its own, separate list of moderators, rather than making use of the `/mods` list in Twitch chat. This is something I plan to change in the future.
- `!quit` and `!kill`: close AkzelBot


Note: AkzelBot has, so far, only been tested on Linux.

## Credit:
Based on BadNidalee's bot: https://github.com/BadNidalee/ChatBot
