import numpy as np
import matplotlib.pyplot as plt
kategorie = ['A', 'B', 'C', 'D']
udzial = [30, 20, 25, 25]
plt.pie(udzial, labels=kategorie,
autopct='%1.f%%', startangle=90,
colors=['skyblue', 'lightgreen',
'lightcoral', 'gold'])
plt.title('Udział w kategoriach')
plt.show()