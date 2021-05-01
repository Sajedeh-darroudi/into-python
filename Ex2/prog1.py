def prog1(a, b):
    even_numbers = []
    for i in range(a, b):
        if i % 2 == 0:
            even_numbers.append(i)
            if even_numbers[0] == a:
                even_numbers.remove(a)
    return even_numbers
