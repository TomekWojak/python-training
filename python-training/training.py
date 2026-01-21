def zliczLitery(tekst):
    slownikLiter = {}
    for litera in tekst:
        if(litera in slownikLiter):
            slownikLiter[litera] += 1
        else:
            slownikLiter[litera] = 1
    print(slownikLiter)

