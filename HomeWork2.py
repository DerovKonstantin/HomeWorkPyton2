
# 1.На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной.

import random

coins = []
head_coins = 0
tails_coins = 0 #решка
number_of_coins = int(input('Введите общее количество монет на столе:'))
for i in range(number_of_coins):
    coins.append(random.randint(0, 1))
    if coins[i] == 1:
        tails_coins += 1
    else:
        head_coins += 1 
print(coins)
if head_coins < tails_coins:
    print('минимальное число монеток, которые нужно перевернуть, c гербом - ', head_coins)
else:
    print('минимальное число монеток, которые нужно перевернуть, c решкой - ', tails_coins)

#-----------------------------------------------------------------------------------------

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

try:
    print('Помогите Кате отгадать задуманные Петей числа')
    first_num = int(input('Введите первое число: - '))
    second_num = int(input('Введите второе число: - '))
    flag = True
    while flag:
        for x in range(1000):
            y = first_num - x
            if x <= y and x * y == second_num:
                print("Загаданные числа ", x, " и ", y)
                flag = False 
except:
    print("Введены некорректные данные")

#------------------------------------------------------

# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числавида 2k), не превосходящие числа N.

num = int(input('Требуется вывести все целые степени двойки не превосходящие числа N, введите число (N): - '))
i = 0
x = 0
flag = True
while flag:
    x = 2**i
    i+=1
    if x > num:
        flag = False
    else:
        print(x)

#----------------------------------------------------

# Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . Но теперь количество предикатов
# не три, а генерируется случайным образом от 5 до 25, сами значения предикатов 
# случайные, проверяем это утверждение 100 раз, с помощью модуля time выводим на экран, 
# сколько времени отработала программа. В конце вывести результат проверки истинности 
# этого утверждения.
    
# не (a и b) = (не a) или (не b)
# не (a или b) = (не a) и (не b)

import time

try:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    predicates_and_meanings ={}
    predicates_num = int(input('Введите колличество предикатов, от 5 до 25: - '))

    while predicates_num < 5 or predicates_num > 25:
        print('Введены некорректные данные')
        predicates_num = int(input('Введите колличество предикатов, от 5 до 25: - '))
    else:
        count = 1
        start = time.time()
        while count < 101:
            print('Попытка № ', count)
            for i in letters[:predicates_num]:
                predicates_and_meanings[i] = random.randint(0, 1)
            print(predicates_and_meanings)
        
            check = []
            for i in predicates_and_meanings:
                a = predicates_and_meanings[i]
                check.append(i)
                for j in predicates_and_meanings:
                    if check.count(j) == 0:
                        b = predicates_and_meanings[j]
                        print(i,j,not(a and b) == ((not a) or (not b)), end = " ")
                print()
            count += 1
        end = time.time() - start
        print('Время работы составило: - ', end)
except:
    print("Введены некорректные данные")
