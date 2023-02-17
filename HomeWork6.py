from random import randint
import random

# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(a, difference, number_of_elements):
    list_a = []
    nth_member = 0
    for i in range(1, number_of_elements+1):
        nth_member = a + (i-1) * difference
        list_a.append(nth_member)
    return list_a

print('Заполнение массива элементами арифметической прогрессии')
first_num = int(input('Введите первый элемент прогрессии: - '))
difference = int(input('Введите разность: - '))
number_of_elements = int(input('Введите колличество элементов: - '))
print(arithmetic_progression(first_num, difference, number_of_elements))

#----------------------------------------------------------------------

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

print('Определить индексы элементов массива в заданном диапазоне')
try:
    random_list = []
    #min_size = 5
    #max_size = 20
    indexes_range = []

    min_size = int(input('Введите минимальное значение диапзона: - '))
    max_size = int(input('Введите максимальное значение диапзона: - '))
    random_element = str(input('Введите элементы списка через пробел: - ')).split()
    random_list = [int(i) for i in random_element]
    for id, item in enumerate(random_list):
        if item >= min_size and max_size >= item:
            indexes_range.append(id)

    print(indexes_range)

except:
    print('Введены некорректные данные.')

# Задача HARD SORT необязательная.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

print('Отсортировать элементы по возрастанию слева направо и сверху вниз')
columns = int(input('Введите колличество столбцов: - '))
rows = int(input('Введите колличество строк: - '))

def creating_random_matrix(columns, rows):
    size = columns * rows
    matrix = [[0] * columns for i in range(rows)]
    random_list = random.sample(range(1, size +1), size)
    coun = 0
    for i in range(columns):
        for j in range(columns):
            matrix[i][j] = random_list[coun]
            coun +=1
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

def sorting_matrix_elements(matrix):
    list_to_sort = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            list_to_sort.append(matrix[i][j])
    list_to_sort.sort()
    coun = 0
    for i in range(columns):
        for j in range(columns):
            matrix[i][j] = list_to_sort[coun]
            coun +=1
    return matrix

matrix = creating_random_matrix(columns, rows)
print_matrix(matrix)
print()

sorting_matrix = sorting_matrix_elements(matrix)
print_matrix(sorting_matrix)

#----------------------------------------------------------------------

# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры), 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и только 
# один раз переместился на другое место и выполнить это за m*n / 2 итераций. То есть если 
# массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести 
# на экран как таблицу.

print('Перемешать случайным образом элементы массива')
columns = int(input('Введите колличество столбцов: - '))
rows = int(input('Введите колличество строк: - '))

def creating_matrix(columns, rows):
    size = columns * rows
    matrix = [[0] * columns for i in range(rows)]
    num_list = [i for i in range(1, size +1)]
    coun = 0
    for i in range(columns):
        for j in range(columns):
            matrix[i][j] = num_list[coun]
            coun +=1
    return matrix
   
def mixer_matrix_elements(matrix):
    #size = len(matrix) * len(matrix[0])
    matrix_converted_to_list = []
    #matrix_mixer_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_converted_to_list.append(matrix[i][j])
    #mixer_index_list = random.sample(range(size), size)
    #for i in range(0, size, 2): 
    #    j = mixer_index_list[i]
    #    c = mixer_index_list[i+1]
    #    matrix_mixer_list.append(matrix_converted_to_list[j])
    #    matrix_mixer_list.append(matrix_converted_to_list[c])
    random.shuffle(matrix_converted_to_list, random.random)
    coun = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] =  matrix_converted_to_list[coun]
            coun +=1
    return matrix

first_matrix = creating_matrix(columns, rows)
print_matrix(first_matrix)
print()

mixer_matrix = mixer_matrix_elements(first_matrix)
print_matrix(mixer_matrix)

#--------------------------------------------
