from random import *
from calc import evaluate
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 9)
    y = randint(0, 9)
    error = randint(-1, 1)
    r = x + y + error
    return [x, y, "+", r]

def check_answer(x, y, op, result, user_choice): #result: ketquahienthitrenmanhinh
    #user_choice: nguoi dung dang click vao dau
    if user_choice == True: 
        if x + y == result:
            return True 
        else: 
            return False 
    else: 
        if x + y != result:
            return True
        else:
            return False 
    pass
