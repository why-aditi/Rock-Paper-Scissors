import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissor: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "Tie"

    if win(user, computer):
        return "You Win!"

    return "You Lost"


def win(p, o):
    if (p == "r" and o == "s") or (p == "p" and o == "r") or (p == "s" and o == "p"):
        return True
    else:
        return False


print(play())
