
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

N = int(input('Требуется вычислить, сколько раз встречается число в массиве. Введите число : - '))
A = [randint(1, 100) for i in range(101)]
X = 0
for i in A:
    if N == i:
        X += 1
print(A)
print('Колличество совпадений: - ', X)

#----------------------------------------

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

N = int(input('Требуется найти в массиве самый близкий элемент к заданному числу. Введите число : - '))
A = [randint(1, 100) for i in range(10)]
X = 0

if N > max(A):
    X = max(A)
elif N < min(A):
    X = min(A)
else:
    max_closes = max(A)
    min_closes = min(A)
    for i in A:
        if min_closes <= i and i <= N:
            min_closes = i
        elif max_closes >= i and i >= N:
            max_closes = i
    if max_closes - N > N - min_closes:
        X = min_closes
    elif max_closes - N == N - min_closes:
        X = str(min_closes,' и ', max_closes)
    else:
        X = max_closes
    
print(A)
print('Cамый близкий элемент к заданному числу: - ', X)
#------------------------------------------------------------------------------

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

try:
    letters_eng_1_point = '1 AEIOULNSTR'
    letters_eng_2_point = '2 DG'
    letters_eng_3_point = '3 BCMP'
    letters_eng_4_point = '4 FHVWY'
    letters_eng_5_point = '5 K'
    letters_eng_8_point = '8 JX'
    letters_eng_10_point = '10QZ'
    letters_rus_1_point = '1 АВЕИНОРСТ'
    letters_rus_2_point = '2 ДКЛМПУ'
    letters_rus_3_point = '3 БГЁЬЯ'
    letters_rus_4_point = '4 ЙЫ'
    letters_rus_5_point = '5 ЖЗХЦЧ'
    letters_rus_8_point = '8 ШЭЮ'
    letters_rus_10_point = '10ФЩЪ'

    alphabet = [letters_eng_1_point, letters_eng_2_point, letters_eng_3_point,
                letters_eng_4_point, letters_eng_5_point, letters_eng_8_point,
                letters_eng_10_point, letters_rus_1_point, letters_rus_2_point,
                letters_rus_3_point, letters_rus_4_point, letters_rus_5_point,
                letters_rus_8_point, letters_rus_10_point]
    
    alphabet_and_glasses ={}
    for i in alphabet:
        for j in i[2:]:
            alphabet_and_glasses[j] = str(i[:2])
    #print(alphabet_and_glasses)

    text = str(input('Введите слово любыми буквами: - '))
    text = text.upper()
    #print(text)
    
    value_entered_word = 0
    for i in text:
        for j in alphabet_and_glasses:
            if j == i:
                value_entered_word += int(alphabet_and_glasses[j])
    print('Cтоимость введенного пользователем слова: - ', value_entered_word)
except:
    print("Введены некорректные данные")    

#------------------------------------------------------------

# Задача HARD необязательная Имеется список чисел. Создайте список, 
# в который попадают числа, описывающие максимальную возрастающую 
# последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
#Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

print('Имеется список чисел. Создайте список, описывающие максимальную возрастающую последовательность')

there_is_list = [randint(1, 10) for i in range(10)]
check_list = []
ascending_sequence_list = []
sum_max = 0
check_list.append(there_is_list[0])
for i in range(1, len(there_is_list)):
    if there_is_list[i] > there_is_list[i-1]:
        check_list.append(there_is_list[i])
        if len(check_list) > 1:
            sum_list = 0
            for j in check_list:
                sum_list += j
                if sum_list > sum_max:
                    sum_max = sum_list
                    ascending_sequence_list = check_list.copy()
        
    elif there_is_list[i] <= there_is_list[i-1]:
        if len(check_list) < 2:
            check_list.clear()
            check_list.append(there_is_list[i])
        else:
            sum_list = 0
            for j in check_list:
                sum_list += j
                if sum_list > sum_max:
                    sum_max = sum_list
                    ascending_sequence_list = check_list.copy()
                    check_list.clear()
                    check_list.append(there_is_list[i])
                else:
                    check_list.clear()
                    check_list.append(there_is_list[i])

print('Имеющийся список', there_is_list)
print('Максимальная возрастающая последовательность',ascending_sequence_list)
