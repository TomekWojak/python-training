def test():
    licznik = 0
    while True:
        x = int(input('Podaj liczbę: '))
        print('wpisana liczba', x)
        if(x > 0): licznik += 1
        if(x == 0): break
    print(licznik)

test()