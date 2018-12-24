def get_even_list(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

# t = get_even_list([1, 4, 5, -1, 10])

# print(t)