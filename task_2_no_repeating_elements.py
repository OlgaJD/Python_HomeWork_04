# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def get_list():
    user_list =[(int(input(f"Введите элемент {i+1} спика: ")))for i in range(int(input('Введите длину списка: ')))]
    return user_list

def find_norepeating_elements ():
    elem_list = get_list()
    for i in elem_list:
        count = 0
        for j in elem_list:
            if i == j:
                count +=1
            if count == 2:
                break
        if count == 1:
            print(i, end=' ')

try:
    find_norepeating_elements()
except:
    print('Вводите только числа. Длина списка должна быть целым числом')