
from random import randint

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

print('Даны два набора чисел, определить числа встречающиеся в обоих наборах')
first_num = int(input('Введите кол-во элементов первого набора: - '))
second_num = int(input('Введите кол-во элементов второго набора: - '))
first_list = [randint(1, 10) for i in range(first_num)]
second_list = [randint(1, 10) for i in range(second_num)]
repetition_list =[]

repetition_list = set(sorted(first_list)).intersection(set(sorted(second_list)))

print(first_list)
print(second_list)
print(repetition_list)

#-------------------------------------------

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
# ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

print('Найдем максимальное число ягод, собирающего модуля')
bed_size = int(input('Введите размер грядки (не меньше 3): - '))
garden_bed = [randint(1, 10) for i in range(1, bed_size +1)]
bed_number = 0
maximum_berries = 0

for i in range(1, len(garden_bed)-1):  
    check_berries = garden_bed[i-1] + garden_bed[i] + garden_bed[i+1]
    if check_berries > maximum_berries:
        maximum_berries = check_berries
        bed_number = i+1

print(garden_bed)
print('Номер грядки', bed_number)
print('Максимальное число ягод', maximum_berries)

#--------------------------------------------------

# задача RLE необязательная. Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных 
# (где только буквы присутствуют для простоты).
# например декодирование

print('Реализуем модуль сжатия и восстановления данных')
set_url = []
sum_letters = 1
set_of_letters = str(input('Введите текст или просто буквы для сжатия и восстановления: - '))
for i in range(1, len(set_of_letters)):
    if set_of_letters[i-1] == set_of_letters[i]:
        sum_letters +=1
        if (i+2) > len(set_of_letters):
            set_url.append(str(sum_letters))
            set_url.append(set_of_letters[i-1])
    elif set_of_letters[i-1] != set_of_letters[i]:
        if sum_letters > 1:
            set_url.append(str(sum_letters))
            set_url.append(set_of_letters[i-1])
        else:
            set_url.append(set_of_letters[i-1])
        sum_letters = 1
if set_of_letters[len(set_of_letters)-1] != set_of_letters[len(set_of_letters)-2]:
    set_url.append(set_of_letters[len(set_of_letters)-1])
    print(''.join(set_url))
else:
    print(''.join(set_url))

set_of_letters = []
for i in range(len(set_url)):
    if str(set_url[i]).isnumeric():
        j = 1
        while j < int(set_url[i]):
            set_of_letters.append(set_url[i+1])
            j += 1
    if str(set_url[i]).isalpha():
        set_of_letters.append(set_url[i])
print(''.join(set_of_letters))








