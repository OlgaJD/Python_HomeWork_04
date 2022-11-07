# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


## Для числа Пи

from math import pi

def found_pi (n): return round(pi, n)
n =  int(input("Введите точность после запятой для числа π: "))
print(f'π = {round(pi, n)}')

#-------------------------------------------------------------------#

# x = float(input('Введите число: '))
# d = float(input('Как будем округлять: '))
# if d == 1:
#     print(int(x))
# else:
#     d = str(d)
#     d = d.split('.')
#     d = len(d[1])
#     print(round(x, d))