import numpy as np
import matplotlib.pyplot as plt
# Zad 1
produkty = ['Mleko', 'Chlyb', 'Woda', 'Warzywa', 'Owoce', 'Słodycze']
iloscSprzedanych = [100, 250, 150, 110,203,303]
plt.bar(produkty, iloscSprzedanych)
plt.show()

# Zad 2
plt.pie(iloscSprzedanych, labels=produkty,
autopct='%1.f%%', startangle=90,
colors=['skyblue', 'lightgreen',
'lightcoral', 'gold'])
plt.title('Udział w kategoriach')
plt.show()

# Zad 3
czas = [1, 2, 3, 4, 5]
prChwilowa = [2, 4, 6, 8, 10]
plt.scatter(czas, prChwilowa)
plt.show()
