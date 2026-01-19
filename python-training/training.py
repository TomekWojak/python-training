iloscWczytywanychLiczb = 5
licznik = 1
suma = 0

def obliczSrednia(suma):
    srednia = suma / iloscWczytywanychLiczb
    print(suma)
    return srednia

while licznik <= 5:
    try:
        x = int(input('Podaj liczbę: '))
        suma += x
        licznik += 1
    except ValueError:
        print('Podano nieprawidłową wartość')

print(obliczSrednia(suma))