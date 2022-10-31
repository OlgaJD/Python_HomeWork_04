# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple (number):
    result = []
    i = 2
    while i <= number:
        if number % i ==0:
            result.append(i)
            number = number / i
        else: i +=1
    return result 

try:
    n = int(input('Введите целое число: '))        
    print(f'Cписок простых множителей числа {n}: {simple(n)}')
except:
    print('Вводите только целые числа')
