def slow(t):
    from time import sleep
    for i in t:
        print(i, end="", flush=True)
        sleep(0.07)


def fivec():
    print(" O")
    print("\|/")
    print(" | ")
    print("/ \ ")


def fourc():
    print(" O")
    print("\|/")
    print(" | ")
    print("/ ")


def threec():
    print(" O")
    print("\|/")
    print(" | ")


def twoc():
    print(" O")
    print("\|")


def onec():
    print("O")
    print("|")


def zeroc():
    slow("GAME OVER \n")
    print(" (X) ")
    print(" \|/")
    print("  | ")
    print(" / \ ")


def winwin():
    slow("You saved the man, you will forever be the hero in the  legends \n")
    print(" (^) ")
    print(" \|/")
    print("  | ")
    print(" / \ ")


import random

wlist = ["twitch", "earthquake", "critical", "delicate", "nightmare", "effect", "doubt", "need", "portion", "chase",
         "car", "jazz", "refrigerator", "orientation", "knee", "advocate", "absurd"]
random.shuffle(wlist)
answer = list(wlist[0])
d = []
u = []
d.extend(answer)
u.extend(d)
for i in range(len(d)):
    d[i] = "_"
slow(" ".join(d))
c = 0
inc = 5
while c < len(answer) and inc > 0:
    guess = input("Enter a letter: ")
    for i in range(len(answer)):
        if answer[i] == guess and guess in u:
            d[i] = guess
            c += 1
            u.remove(guess)
    if guess not in d:
        inc -= 1
        slow(f"Wrong guess , try again. You now have {inc} guesses")
        print()
    slow(f"You guessed {c} letters \n")
    if inc == 5:
        fivec()
    elif inc == 4:
        fourc()
    elif inc == 3:
        threec()
    elif inc == 2:
        twoc()
    elif inc == 1:
        onec()
    print()
    print(" ".join(d))
    print()
if c == len(answer):
    winwin()

else:
    zeroc()
    slow(" RIP")