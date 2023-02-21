
import random

# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

print('Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.')
poem = str(input('Винни-Пух вбивает Стихотворение(пара-ра-рам рам-пам-папам па-ра-па-дам): - '))

#poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
#vowel_letters = 'аяуюоеёэиы'
#letter_counter = 0
#for i in poem_list:
#    print('i',i)
#    for j in i:
#        print('j',j)
#        if j in vowel_letters:
#            letter_counter += 1
#    letter_counter_list.append(letter_counter)
#    letter_counter = 0

def phrase_check(x):
    letter_counter = 0
    vowel_letters = 'аяуюоеёэиы'
    for i in x:
        if i in vowel_letters:
            letter_counter += 1
    return letter_counter

def rhythm_check(counter_list):
    if min(counter_list) == max(counter_list):
        print('Парам пам-пам')
    else:
        print('Пам парам')

poem_list = poem.split()
letter_counter_list = (list(map(phrase_check, poem_list)))
rhythm_check(letter_counter_list)

#----------------------------------------------------------

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, x, y):
    matrix = []
    list_matrix =[]

    for i in range(1, x+1):
        list_matrix.append(i)
        print(i, end=" ")
    matrix.append(list_matrix.copy())
    list_matrix.clear()
    print()

    for i in range(2, y+1):
        list_matrix.append(i)
        print(i, end=" ")
        for j in range(2, x+1):
            result = operation(i, j)
            list_matrix.append(result)
            print(result, end=" ")
        matrix.append(list_matrix.copy())
        list_matrix.clear()
        print()
    return matrix

print('функция которая принимает в качестве аргумента функцию')
columns = int(input('Введите колличество столбцов: - '))
rows = int(input('Введите колличество строк: - '))
char = str(input('Обозначте тип арифметической операции : -, +, *, / '))

if char == '-':
    operation = lambda x, y: x - y
    print_operation_table(operation, columns, rows)
elif char == '+':
    operation = lambda x, y: x + y
    print_operation_table(operation, columns, rows)
elif char == '*':
    operation = lambda x, y: x * y
    print_operation_table(operation, columns, rows) 
elif char == '/':
    operation = lambda x, y: x / y
    print_operation_table(operation, columns, rows)
else:
    print('Введен неверный символ')

#---------------------------------------------------------

# Необязательное задание - сделать локальный чат-бот с хранилищем данных в формате JSON, 
# как объясняли в приложенной записи буткемпа.