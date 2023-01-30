# Задача 2: Найдите сумму цифр трехзначного числа.

sum_digits_number = str(input("Введите натуральное число: - "))
sum_digits = 0

for i in sum_digits_number:
    sum_digits = sum_digits + int(i)

print(sum_digits)

#-------------------------------------------------------

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number_of_products = int(input("Введите колличество журавликов: - "))
number_of_products_M = number_of_products //4

print("Петя и Сережа сделают по - ", number_of_products_M, 
" журавликов, Катя сделала в два раза больше - ", number_of_products - number_of_products_M *2)

#-------------------------------------------------------

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
# за проезд и получали билет с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. 
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.

ticket_number = str(input("Введите номер билета: - "))
first_three = 0
last_three = 0

for i in ticket_number[:3]:
    first_three = first_three + int(i)
for i in ticket_number[3:]:
    last_three = last_three + int(i)
if first_three == last_three:
    print("Билет счастливый")
else:
    print("Не счастливый билет, в следующий раз обязательно повезет")

#-------------------------------------------------------

# Задача 8: Требуется определить, можно ли от шоколадки размером n ? m 
# долек отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

the_size_n = int(input("Введите размер шоколадки (n) : - "))
the_size_m = int(input("Введите размер шоколадки (m) : - "))

if the_size_n <= 1 and the_size_m <= 1:
    print("Размер шоколадки слишком мал")
else:    
    size_of_slices = int(input("Введите колличество отламываемых долек (k) : - "))

    if the_size_n <= the_size_m:
        min_size = the_size_n
        max_size = the_size_m
        if size_of_slices >= min_size and size_of_slices <= max_size * min_size - min_size:###
            if size_of_slices % the_size_n == 0 or size_of_slices % the_size_m == 0:
                print("Можно разломить шоколадку на два прямоугольника")
            else:
                print("Разломить шоколадку на два прямоугольника нельзя")
        else:
            print("Разломить шоколадку на два прямоугольника нельзя")
    else:
        min_size = the_size_m
        max_size = the_size_n
        if size_of_slices >= min_size and size_of_slices <= max_size * min_size - min_size:###
            if size_of_slices % the_size_n == 0 or size_of_slices % the_size_m == 0:
                print("Можно разломить шоколадку на два прямоугольника")
            else:
                print("Разломить шоколадку на два прямоугольника нельзя")
        else:
            print("Разломить шоколадку на два прямоугольника нельзя 2.1")

#-------------------------------------------------------

# Задача 2: - HARD необязательная, идет за 3 обязательных. 
# Найдите сумму цифр любого вещественного или целого числа. 
# Можно использовать decimal. Через строку решать нельзя.

try:
    num = float(input("Введите вещественное или целое число: - "))
    sum = 0
    x = 10
    if num < 0:
        num *= -1
        num_x = num
        while num_x > int(num_x):
            num_x = num
            num_x *= x
            x *= 10
        while num_x > 0:
            sum += int(num_x)%10
            num_x //= 10
    else:
        num_x = num
        while num_x > int(num_x):
            num_x = num
            num_x *= x
            x *= 10
        while num_x > 0:
            sum += int(num_x)%10
            num_x //= 10
    print(sum)
except:
    print("Введены некорректные данные")