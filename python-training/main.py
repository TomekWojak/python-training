x = str(3)
y = int(3)
z = float(3)

print(x,type(x),y, type(y),z)


numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if(i % 2 == 0): print(f'{i} jest liczbą parzystą')

# even counter
def evenCounter():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f'Parzyste: {even_count} \nNieparzyste: {odd_count}')

evenCounter()

# products shop

def makeShopping():
    products = {"jabłko": 2.5, "banan": 3.2, "chleb": 5.0, "mleko": 4.5}
    total = 0

    while True:
        product = input('Podaj produkt (lub wpisz "koniec"): ')
        
        if product == "koniec":
            break
        elif product in products:
            total += products[product]
        else:
            print("Nie ma takiego produktu!")

    print(f'Suma zakupów: {total} zł')

# makeShopping()

# average grade
grades = {"Ala": 5, "Bartek": 4, "Celina": 3, "Dawid": 5, "Ewa": 2}


def calculateTheAverage():
    return sum(grades.values()) / len(grades)


def classifyStudents():
    average = calculateTheAverage()

    for name, grade in grades.items():
        if(grade > average):
            print(f'Powyżej średniej: {name}')
        elif(grade < average):
            print(f'Poniżej średniej: {name}')
        else:
            print(f'Równo ze średnią: {name}')

classifyStudents()

def miniCalc():
    a = int(input('Podaj liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    operator = input('Podaj operator: ')

    if(operator != "+" and operator != "-" and operator != "/" and operator != "*"):
        print(f'{operator} jest nieprawidłowym operatorem!')
        return
    
    if(operator == "+"):
        result = a + b
    elif(operator == "-"):
        result = a - b
    elif(operator == "/"):
        if b == 0:
            print("Nie można dzielić przez 0!")
            return
        result = a / b
    elif(operator == '*'):
        result = a * b
    
    print(f'Wynik działania {a} {operator} {b} to: {result}')



miniCalc()