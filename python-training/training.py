L = [1,2,3,4,50,10,23,20,22,303,51,65]

def test():
    licznik = 0
    for x in L:
        if x > 10:
            licznik += 1

    return licznik
print(test())