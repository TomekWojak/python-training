def test(text):
    text2 = text[::-1]

    if(text2.lower() == text.lower()):
        print(f'{text} jest palindromem')
    else:
        print(f'{text} nie jest palindromem')
test('KamilSlimak')