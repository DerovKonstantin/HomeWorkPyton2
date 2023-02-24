from random import *
import json

phone_numbers = {}
full_name = {'Имя':'-', 'Фамилия':'-','Отчество': '-', 'Дополнительная информация':'-'}
full_name['Имя'] = 'Константин'
full_name['Фамилия'] = 'Деров'
full_name['Отчество'] = 'Павлович'
phone_numbers['89535813181'] = full_name

def save(phone_numbers):
    with open("phone_numbers.json", "w", encoding = "utf-8") as p_n:
        p_n.write(json.dumps(phone_numbers, ensure_ascii = False))
    print("Номер телефона успешно сохранен в файле phone_numbers.json")

def load():
    with open("phone_numbers.json", "r", encoding = "utf-8") as p_n:
        phone_numbers = json.load(p_n)
    print("Номера телефонов успешно загружены")
    return phone_numbers

def Data_correction(phone_numbers, key):
    num = input('Какие данные хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
    while num.isdigit() == False or int(num) < 1 or int(num) > 5:
        print('Введены некорректные данные.')
        num = input('Какие данные хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
    while int(num) < 5:
        if num == '1':
            print('Старое имя - ', phone_numbers[key]['Имя'])
            phone_numbers[key]['Имя'] = input('Введите новое имя: - ')
            num = input('Какие данные еще хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
            while num.isdigit() == False:
                print('Введены некорректные данные.')
                num = input('Какие данные хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
        elif num == '2':
            print('Старая фамилия - ', phone_numbers[key]['Фамилия'])
            phone_numbers[key]['Фамилия'] = input('Введите новую фамилию: - ')
            num = input('Какие данные еще хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
            while num.isdigit() == False:
                print('Введены некорректные данные.')
                num = input('Какие данные хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
        elif num == '3':
            print('Старое отчество - ', phone_numbers[key]['Отчество'])
            phone_numbers[key]['Отчество'] = input('Введите новое отчество: - ')
            num = input('Какие данные еще хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
            while num.isdigit() == False:
                print('Введены некорректные данные.')
                num = input('Какие данные хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
        elif num == '4':
            print('Имеющяяся информация - ', phone_numbers[key]['Дополнительная информация'])
            phone_numbers[key]['Дополнительная информация'] = input('Введите дополнительную информцию: - ')
            num = input('Какие данные еще хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
            while num.isdigit() == False:
                print('Введены некорректные данные.')
                num = input('Какие данные хотите откорректировать: Имя - 1, Фамилия - 2, Отчество - 3, Дополнительную информацию - 4, Ничего не корректировать - 5. - ')
    return phone_numbers

#text_1 = 'Введите имя: - '
#text_2 = 'Имя'
def Search_and_correction_data(text_1, text_2, phone_numbers):
    check_key = ''
    text = input(text_1)
    while text.isalpha() == False:
        print('Введены некорректные данные.')
        input(text_1)
    for key in phone_numbers:
        name = str(phone_numbers[key][text_2])
        if text.lower() == name.lower():
            check_key = key
            print('Номер телефона - ', key, ', Личные данные - ', phone_numbers[key])
            num = input('Произвести корректировку данных, да - 1, нет - 2. - ')##
            while num.isdigit() == False or int(num) < 1 or int(num) > 2:
                print('Введены некорректные данные.')
                num = input('Произвести корректировку данных, да - 1, нет - 2. - ')
            if num == '1':
                Data_correction(phone_numbers, check_key)
                print('Номер телефона - ', check_key, ', Личные данные - ', phone_numbers[check_key])
                num = input('Произвести повторную корректировку данных, да - 1, нет - 2. - ')
                while num.isdigit() == False or int(num) < 1 or int(num) > 2:
                    print('Введены некорректные данные.')
                    num = input('Произвести повторную корректировку данных, да - 1, нет - 2. - ')
            elif num == '2':
                print('Данные не корректировались.')
    if check_key == '':
        print('Совпадений не обнаружено')
    return phone_numbers

while True:
    command = input('Введите команду: Запуск-1, Остановка-2, Добавление-3, Удаление-4, Все записи-5, Помощь-6, Сохранение-7, Загрузка-8, Поиск - 9. - ')
    while command.isdigit() == False or int(command) < 1 or int(command) > 9:
        print('Введены некорректные данные.')
        command = input('Введите команду: Запуск-1, Остановка-2, Добавление-3, Удаление-4, Все записи-5, Помощь-6, Сохранение-7, Загрузка-8, Поиск - 9. - ')
    if command == '1': # Запуск бота -1
        print('Бот телефонных номеров начал свою работу.')
    elif command == '2': # Остановка бота -2
        num = input('Сохранить данные: Да - 1, Нет - 2: - ')
        while num.isdigit() == False or int(num) < 1 or int(num) > 2:
            print('Введены некорректные данные.')
            num = input('Сохранить данные: Да - 1, Нет - 2')
        if num == '1':
            save(phone_numbers)
            print('Бот остановил свою работу.')
            break
        elif num == '2':
            print('Бот остановил работу без сохранения данных.')
            break 
    elif command == '5': # Весь список -5
        print('Отображон текущий список файлов')
        print(phone_numbers)
    elif command == '3': # Добавление данных -3
        coincidence = False
        number = input('Ведите номер телфона: - ')
        while number.isdigit() == False:
            number = input('Номер должен состоять из цифр. Ведите номер телфона: - ')
        for key in phone_numbers:
            if number == key:
                coincidence = True
                print('Данный номер уже существует.')
                num = input('Выберите действие: проверить даные - 1, откорректировать - 2, оставить как есть - 3. - ')
                while num.isdigit() == False or int(num) < 1 or int(num) > 3:
                    print('Введены некорректные данные.')
                    num = input('Выберите действие: проверить даные - 1, откорректировать - 2, оставить как есть - 3. - ')
                if num == '1':
                    print(phone_numbers[key])
                    num = input('Выберите действие: откорректировать - 2, оставить как есть - 3. - ')
                    while num.isdigit() == False or int(num) < 2 or int(num) > 3:
                        print('Введены некорректные данные.')
                        num = input('Выберите действие: откорректировать - 2, оставить как есть - 3. - ')
                    if num == '2':
                        phone_numbers = Data_correction(phone_numbers, key)
                    elif num == '3':
                        print('Данные оставлены без изменения.')
                elif num == '2':
                    phone_numbers = Data_correction(phone_numbers, key)
                elif num == '3':
                    print('Данные оставлены без изменения.')

        if coincidence == False:
            phone_numbers[number] = {}
            phone_numbers[number]['Имя'] = input('Введите имя: - ')
            if phone_numbers[number]['Имя'] == '':
                phone_numbers[number]['Имя'] = '-'
            phone_numbers[number]['Фамилия'] = input('Введите фамилию: - ')
            if phone_numbers[number]['Фамилия'] == '':
                phone_numbers[number]['Фамилия'] = '-'
            phone_numbers[number]['Отчество'] = input('Введите отчество: - ')
            if phone_numbers[number]['Отчество'] == '':
                phone_numbers[number]['Отчество'] = '-'
            phone_numbers[number]['Дополнительная информация'] = input('Введите Дополнительную информацию: - ')
            if phone_numbers[number]['Дополнительная информация'] == '':
                phone_numbers[number]['Дополнительная информация'] = '-'
    elif command == '6': # Помощь -6
        print('Запуск бота-1, Остановка бота-2, Добавление данных-3, Удаление данных-4, Весь список-5, Помощь-6, Сохранение данных-7, Загрузка данных-8.')  
    elif command == '4': # Удаление данных -4
        number = input('Ведите номер телфона подлежащий удалению: - ')
        for key in phone_numbers:
            if number == key:
                del phone_numbers[key]
                print('Номера - ', number, ' найден и удален.')
                break
        else:
            print('Такого номера нет')   
    elif command == '7': # Сохранение данных -7
        save(phone_numbers) 
    elif command == '8': # Загрузка данных -8
        phone_numbers = load()
    elif command == '9': # Поиск данных -9
        #checklist = {}
        num = input('Выберите параметры поиска: по номеру -1, по имени -2, по фамилии -3, по отчеству -4, выход -5. - ')
        while num.isdigit() == False or int(num) < 1 or int(num) > 5:
            print('Введены некорректные данные.')
            num = input('Выберите параметры поиска: по номеру -1, по имени -2, по фамилии -3, по отчеству -4, выход -5. - ')
        while int(num) > 1 or int(num) < 5:
            if num == '1':
                number = input('Введите номер: - ')
                while num.isdigit() == False:
                    print('Введены некорректные данные.')
                    input('Введите номер: - ')
                for key in phone_numbers:
                    if number == key:
                        check_key = key
                        print(phone_numbers[key])
                Data_correction(phone_numbers, check_key)
                num = input('Для выхода нажмите 5, для продолжения поиска выберите парамет: по номеру -1, по имени -2, по фамилии -3, по отчеству -4. - ')
                while num.isdigit() == False or int(num) < 1 or int(num) > 5:
                    print('Введены некорректные данные.')
                    num = input('Выберите параметры поиска: по номеру -1, по имени -2, по фамилии -3, по отчеству -4, выход -5. - ')
            elif num == '2':
                text_1 = 'Введите имя: - '
                text_2 = 'Имя'
                phone_numbers = Search_and_correction_data(text_1, text_2, phone_numbers)
                num = input('Для выхода нажмите 5, для продолжения поиска выберите парамет: по номеру -1, по имени -2, по фамилии -3, по отчеству -4. - ')
                while num.isdigit() == False or int(num) < 1 or int(num) > 5:
                    print('Введены некорректные данные.')
                    num = input('Выберите параметры поиска: по номеру -1, по имени -2, по фамилии -3, по отчеству -4, выход -5. - ')
            elif num == '3':
                text_1 = 'Введите фамилию: - '
                text_2 = 'Фамилия'
                phone_numbers = Search_and_correction_data(text_1, text_2, phone_numbers)
                num = input('Для выхода нажмите 5, для продолжения поиска выберите парамет: по номеру -1, по имени -2, по фамилии -3, по отчеству -4. - ')
                while num.isdigit() == False or int(num) < 1 or int(num) > 5:
                    print('Введены некорректные данные.')
                    num = input('Выберите параметры поиска: по номеру -1, по имени -2, по фамилии -3, по отчеству -4, выход -5. - ')
            elif num == '4':
                text_1 = 'Введите отчество: - '
                text_2 = 'Отчество'
                phone_numbers = Search_and_correction_data(text_1, text_2, phone_numbers)
                num = input('Для выхода нажмите 5, для продолжения поиска выберите парамет: по номеру -1, по имени -2, по фамилии -3, по отчеству -4. - ')
                while num.isdigit() == False or int(num) < 1 or int(num) > 5:
                    print('Введены некорректные данные.')
                    num = input('Выберите параметры поиска: по номеру -1, по имени -2, по фамилии -3, по отчеству -4, выход -5. - ')
            break
        

