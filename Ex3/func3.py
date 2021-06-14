def func3(C):
    St = "{}".format(C)
    res = 0
    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for i in St:
        if St.index(i) < St.index("."):
            res = res * 10 + value[i]
        else:
            break
    return res

C = 114.7446
print(func3(C))
