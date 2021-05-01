def prog4(a):
    Divisors = []
    for n in range(1, a+1):
        if a % n == 0:
            Divisors.append(n)
    return Divisors
