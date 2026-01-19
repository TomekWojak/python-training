temps = [10,0,-3,-5,15,21,-20,-50]
ujemne = []

def test():
    for i in temps:
            if i < 0:
                ujemne.append(i)

test()
print(ujemne)
