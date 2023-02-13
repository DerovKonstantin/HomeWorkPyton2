
# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

print('программа возводит число А в целую степень B')
A, B = int(input('Введите число А: - ')), int(input('Введите число Б: - '))

def number_to_powe(a, b):
    if b == 1:
        return a
    else:
        return a * number_to_powe(a, b -1)

print(number_to_powe(A, B))

#---------------------------------------

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

print('программа возвращает сумму двух целых неотрицательных чисел')
A, B = int(input('Введите число А: - ')), int(input('Введите число Б: - '))

def sum_of_numbers(a, b):
    if b == 0:
        return a
    else:
        return sum_of_numbers(a +1, b -1)

print(sum_of_numbers(A, B))

#------------------------------------------

# Решать только через рекурсию!. Пользоваться встроенными функциями 
# вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел. Надо посчитать 
# результат введенного выражения.
# Например,
# на входе 1+9/3*7-4
# на выходе 18

print('программа считает результат введенного строчьного выражения')
arithmetic_expression = str(input('Введите арифметическое выражение типа(9.9/3+3.5*2-5.3): - '))
arithmetic_expression += ' ' # при определении последнего числа индекс выходит за пределы

from decimal import Decimal

def number_search(text, i, j, num):
    num = text[i:j+1]
    if str(text[i-1]).isnumeric() == False and str(text[j+1]).isnumeric() == False \
        and str(text[i-1]) != "." and str(text[j+1]) != "." :
        return num, i, j
    elif str(text[j+1]) == '.':
        return number_search(text, i, j+1, num)
    elif str(text[i-1]) == '.':
        return number_search(text, i-1, j, num)
    elif str(text[j+1]).isnumeric()== True:
        return number_search(text, i, j+1, num)
    elif str(text[i-1]).isnumeric()== True:
        return number_search(text, i-1, j, num)

def calculator(text, result):
    index = 0
    first_number = ''
    second_number = ''
    i_first = 0
    j_first = 0
    i_second = 0 
    j_second = 0

    print(text)
    if len(text) == len(str(result))+1:
        return result
    
    elif '*' in  str(text):
        index = str(text).find('*')
        first_number, i_first, j_first = number_search(text, index-1, index-1, '')
        second_number, i_second, j_second = number_search(text, index+1, index+1, '')
        result = Decimal(first_number) * Decimal(second_number)
        text = str(text).replace(str(text[i_first:j_second+1]), str(result))
        return calculator(text, result)

    elif '/' in  str(text):
        index = str(text).find('/')
        first_number, i_first, j_first = number_search(text, index-1, index-1, '')
        second_number, i_second, j_second = number_search(text, index+1, index+1, '')
        result = Decimal(first_number) / Decimal(second_number)
        text = str(text).replace(str(text[i_first:j_second+1]), str(result))
        return calculator(text, result)

    elif '+' in  str(text):
        index = str(text).find('+')
        first_number, i_first, j_first = number_search(text, index-1, index-1, '')
        second_number, i_second, j_second = number_search(text, index+1, index+1, '')
        result = Decimal(first_number) + Decimal(second_number)
        text = str(text).replace(str(text[i_first:j_second+1]), str(result))
        return calculator(text, result)

    elif '-' in  str(text):
        index = str(text).find('-')
        first_number, i_first, j_first = number_search(text, index-1, index-1, '')
        second_number, i_second, j_second = number_search(text, index+1, index+1, '')
        result = Decimal(first_number) - Decimal(second_number)
        text = str(text).replace(str(text[i_first:j_second+1]), str(result))
        return calculator(text, result)
    
calculator(arithmetic_expression, 0)
