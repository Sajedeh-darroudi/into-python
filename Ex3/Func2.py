def Func2(B):
    res = 0
    LastItem = len(B)
    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for i in B:
        if i != '.':
            res = res * 10 + value[i]
            Pos1 = B.index(".")
            Pos2 = LastItem -1
            Pos = Pos2 - Pos1
            A = res / 10**Pos
    return A

B = "145.745568"
print(Func2(B))
