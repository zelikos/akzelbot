import random

def grab_pun():
    pun = ""
    try:
        with open("punList.txt", mode = "r") as f:
            punList = [line.strip() for line in f]
        return random.choice(punList)
        f.close()
    except FileNotFoundError:
        return "File not found."


print(grab_pun())
