oceny = [1,2,3,4,5]
def test():
    minimum = oceny[0]
    for x in oceny:
        if x < minimum:
            minimum = x

    return  minimum

print(test())
