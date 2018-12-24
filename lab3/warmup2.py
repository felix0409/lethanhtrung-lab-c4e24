from calc import *

x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))
op = input("Enter a operator (+, -, *, /)? ")
print(op)

# if op == "+":
#     r = evaluate(x, y)
# elif op == "-":
#     r = evaluate(x, y)
# elif op == "x":
#     r = evaluate(x, y)
# else:
#     r = evaluate(x, y)

r = evaluate(op, x, y)
print(r)


