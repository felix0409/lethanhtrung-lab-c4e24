from random import randint
from calc import evaluate

#1. Generate equation

x = randint(0, 9)
y = randint(0, 9)
error = randint(-1, 1)
r = evaluate("+", x, y) + error

print(f"{x} + {y} = {r}")

if error == 0:
    r = True
else:
    r = False

while True:
    user_answer = input("(Y/N)? ").upper()
    if user_answer == "Y":
        user_answer = True
        if user_answer == r:
            print("Yay!")
            break
        else:
            print("Wrong!")
            break
    elif user_answer == "N":
        user_answer = False
        if user_answer == r:
            print("Yay!")
            break
        else:
            print("Wrong!")
            break
    else:
        print("Please type Y/N!")


