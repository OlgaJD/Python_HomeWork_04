# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def make_coeff_list():
    coeff_list = ' = 0'
    k = int(input('Введите натуральную степень: '))
    for i in range(k+1):
        coef = int(random.randint(0, 100))
        if coeff_list != ' = 0':
            coeff_list = ' + ' + coeff_list
        if i == 0:
            coeff_list = str(coef) + coeff_list
        elif i == 1:
            coeff_list = str(coef) + "*x"  + coeff_list
        else:
            coeff_list = str(coef) + "*x^" + str(i)  + coeff_list
    return coeff_list

def make_txt_file(data):
    with open('polynomial.txt', 'w', encoding='utf-8') as f:
        f.write(data)

try:
    primer = make_coeff_list()
    make_txt_file(primer)
    print(f"Выражение: {primer} записано в файл 'polynomial.txt'")
except:
    print("Надо вводить только целые числа")

