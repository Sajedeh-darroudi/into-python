def func4(D):
    NewList = []
    for i in D:
        (a, b) = i
        while b != 0:
            (a, b) = (b, a % b)
        s = (i[0]/a, i[1]/a)
        NewList.append(tuple(s))
    return NewList

D = [(9, 81), (7, 14), (6, 4)]
print(func4(D))
