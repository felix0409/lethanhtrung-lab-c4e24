def is_inside(a, b): #a is a list with x, y respectively
    #b is a list with x,y and width, height of a rectangle
    for i in range(1):
        if (a[i] >= b[i]) and (a[i+1] >= b[i+1]):
            print("This point is inside of a rectangle")
        else:
            print("This point is outside of a rectangle")


# is_inside([20, 30], [20, 20, 30, 30]) >> inside
# is_insode([10, 10], [20, 20, 30, 30]) >> outside

