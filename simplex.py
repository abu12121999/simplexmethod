import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Maqsad funksiyasi va chegara shartlari
c = np.array([4, 2])   # maqsad funksiyasi
A = np.array([[2, -2], [-4, 1], [2, 3]]) # nobazis kataklar
b = np.array([1, 2, 4]) # ozod sonlar

# Minimal yoki maksimal topilishini so'raymiz
a = True
while a:
    question = input("Maqsad funksiyasining qanday qiymatini topmoqchisiz?\n \
[1] - minimal\n \
[2] - maksimal\n \
Kiriting: ")
    if question == "1":
        # Maqsad funksiyasining minimal qiymati
        res = linprog(c=c, A_ub=A, b_ub=b, method='simplex')
        a = False
    elif question == "2":
        # Maqsad funksiyasining maksimal qiymati
        res = linprog(c=-c, A_ub=A, b_ub=b, method='simplex')
        a = False
    else:
        print("Xato varint kiritdiz\n")
# Javobni chop etamiz
print(res)

# Chizish
x = np.arange(0, 2, 0.1)
y1 = (2 - x) / 2
y2 = (1 + 4 * x) / 2

plt.plot(x, y1, label=r'$2x_1 - 2x_2 \leq 1$')
plt.plot(x, y2, label=r'$-4x_1 + x_2 \leq 2$')
plt.fill_between(x, 0, y1, where=y1<=y2, color='grey', alpha=0.5)
plt.fill_between(x, 0, y2, where=y2<=y1, color='grey', alpha=0.5)

# yangi qatorlarni qo'shib chizish
y3 = (-2/3)*x + (4/3)
y4 = (-2/3)*x + (10/3)
plt.plot(x, y3, label=r'$2x_1 + 3x_2 \leq 4$')
plt.plot(x, y4, label=r'$2x_1 + 3x_2 \geq 4$')
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()