def prog3(a):
    Counters = 0
    for i in range(1, a+1):
        if (a % i) == 0:
            Counters += 1
    if Counters == 2:
        a = True
    else:
        a = False
    return a
