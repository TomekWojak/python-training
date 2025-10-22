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
