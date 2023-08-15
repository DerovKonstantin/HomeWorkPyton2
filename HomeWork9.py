
from datetime import datetime
from random import *
import json

# переводим формат даты в формат строки для создания ключа заметки
def convertDateToText(datetime):
    dt = datetime
    return ' '.join([str(dt.year), str(dt.month), str(dt.day), str(dt.hour), str(dt.minute), str(dt.second), str(dt.microsecond)])

# переводим формат строки (обозначающую дату) в формат даты для работ с датами
def extractDateFromText(txtdate):
    ts = txtdate.split()
    return datetime(int(ts[0]), int(ts[1]), int(ts[2]), int(ts[3]), int(ts[4]), int(ts[5]), int(ts[6]))

# Создаем базовые заметки
notebook = {}
dt = datetime(2022, 8, 13, 10, 12, 9, 142258)
the_note = {'Название заметки':'-', 'Содержание заметки':'-'}
the_note['Название заметки'] = 'Поход в магазин'
the_note['Содержание заметки'] = 'Купить: - молоко, яйца'
notebook[convertDateToText(dt)] = the_note

dt = datetime(2023, 6, 1, 9, 11, 8, 142251)
the_note = {'Название заметки':'-', 'Содержание заметки':'-'}
the_note['Название заметки'] = 'Поездка на отдых'
the_note['Содержание заметки'] = 'Собратся и поехать'
notebook[convertDateToText(dt)] = the_note

dt = datetime(2023, 8, 11, 9, 11, 8, 142251)
the_note = {'Название заметки':'-', 'Содержание заметки':'-'}
the_note['Название заметки'] = 'Поход в поход'
the_note['Содержание заметки'] = 'купить все необходимое'
notebook[convertDateToText(dt)] = the_note

# Сохранение файла с записями
def save(notebook):
    with open("Notebook.json", "w", encoding = "utf-8") as nb:
        nb.write(json.dumps(notebook, ensure_ascii = False))
    print("Записи успешно сохранен в файле Notebook.json")

# Загрузка файла 
def load():
    with open("Notebook.json", "r", encoding = "utf-8") as nb:
        notebook = json.load(nb)
    print("Номера телефонов успешно загружены")
    return notebook

# Ввод числа и проверка на соответствие числу
def checkInputNumber(txt1, txt2, minnum, maxnum):
    num = input(txt1)
    while num.isdigit() == False or int(num) < minnum or int(num) > maxnum:
        print(txt2)
        num = input(txt1)
    return num

# Корректировка имеющихся записей
def dataCorrection(notebook, key):
    txt1 = 'Какие данные хотите откорректировать: Название заметки - 1, Содержание заметки - 2, Ничего не корректировать - 0. - '
    txt2 = 'Введены некорректные данные.'
    num = checkInputNumber(txt1, txt2, 0, 2)
    while int(num) <= 2:
        if num == '1':
            print('Старое название заметки - ', notebook[key]['Название заметки'])
            notebook[key]['Название заметки'] = input('Введите новое название заметки: - ')
            num = checkInputNumber(txt1, txt2, 0, 2)
        elif num == '2':
            print('Старое содержание заметки - ', notebook[key]['Содержание заметки'])
            notebook[key]['Содержание заметки'] = input('Введите новое содержание заметки: - ')
            num = checkInputNumber(txt1, txt2, 0, 2)
        elif num == '0':
            return notebook

# Поиск и корректировка записей
# txt01 = 'Введите название заметки - '
# txt02 = 'Название заметки'
def searchAndCorrectionData(txt01, txt02, notebook):
    txt1 = 'Произвести корректировку данных, да - 1, нет - 2. - '
    txt2 = 'Введены некорректные данные.'
    check_key = ''
    text = input(txt01)
    for key in notebook:
        name = str(notebook[key][txt02])
        if text.lower() == name.lower():
            check_key = key
            print('Найдено совпадение...\n\tДата создания заметки - ', extractDateFromText(key), 
                    '\n\tназвание заметки - ', notebook[key][txt02], 
                    '\n\tсодержание заметки - ', notebook[key]['Содержание заметки'],
                    '\n...')
            num = checkInputNumber(txt1, txt2, 1, 2)
            if num == '1':
                dataCorrection(notebook, check_key)
                print('...\n\tДата создания заметки - ', extractDateFromText(key), 
                    '\n\tназвание заметки - ', notebook[key][txt02], 
                    '\n\tсодержание заметки - ', notebook[key]['Содержание заметки'],
                    '\n...')
                num = checkInputNumber(txt1, txt2, 1, 2)
            elif num == '2':
                print('Данные не корректировались.')
    if check_key == '':
        print('Совпадений не обнаружено')
    return notebook

# Зпуск логики пограммы
while True:
    txt1 = 'Введите команду: Запуск-1, Остановка-2, Добавление-3, Удаление-4, Все записи-5, Помощь-6, Сохранение-7, Загрузка-8, Поиск - 9. - '
    txt2 = 'Введены некорректные данные.'
    txt3 = 'Сохранить данные: Да - 1, Нет - 2: - '
    txt4 = 'Выберите действие: проверить даные - 1, откорректировать - 2, оставить как есть - 0. - '
    txt5 = 'Выберите действие: откорректировать - 1, оставить как есть - 0. - '
    txt6 = 'Помощ...\n\t1) Запуск программы записная книжка\n\t2) Остановка программы записная книжка\n\t3)Добавление новых записей(заметок)\n\t4) Удаление новых записей(заметок)\n\t5) Весь список имеющихся заметок\n\t6) Помощь\n\t7) Сохранение данных\n\t8) Загрузка данных.'
    txt7 = 'Выберите параметры поиска: по дате составления заметки -1, по названию заметки -2 выход -0. - '
    command = checkInputNumber(txt1, txt2, 1, 9)
    if command == '1': # Запуск бота -1
        print('Записная книжка открыта.')
    elif command == '2': # Остановка бота -2
        num = checkInputNumber(txt3, txt2, 1, 2)
        if num == '1': # Запуск-1
            save(notebook)
            print('Записная книжка закрыта.')
            break
        elif num == '2': # Остановка-2
            print('Записная книжка закрыта без новых записей.')
            break 
    elif command == '5': # Весь список -5
        print('Отображон текущий список всех имеющихся заметок')
        print('...')
        for key in notebook:
            print('\t' + notebook[key]['Название заметки'])
        print('...')
    elif command == '3': # Добавление данных -3
        txtmatching = False
        notetitle = input('Ведите название новой заметки: - ')
        for key in notebook:
            if notetitle == notebook[key]['Название заметки']:
                txtmatching = True
                print('Заметка с таким названием уже существует.')
                num = checkInputNumber(txt4, txt2, 0, 2)
                if num == '1':
                    print('...\n\tДата создания заметки - ', extractDateFromText(key), 
                    '\n\tназвание заметки - ', notebook[key]['Название заметки'], 
                    '\n\tсодержание заметки - ', notebook[key]['Содержание заметки'],
                    '\n...')
                    num = checkInputNumber(txt5, txt2, 0, 1)
                    if num == '1':
                        notebook = dataCorrection(notebook, key)
                    elif num == '0':
                        print('Данные оставлены без изменения.')
                elif num == '2':
                    notebook = dataCorrection(notebook, key)
                elif num == '0':
                    print('Данные оставлены без изменения.')
        if txtmatching == False:
            dt = datetime.now()
            dtc = convertDateToText(dt)
            notebook[dtc] = {}
            notebook[dtc]['Название заметки'] = notetitle
            notebook[dtc]['Содержание заметки'] = input('Введите содержание заметки: - ')
            if notebook[dtc]['Содержание заметки'] == '':
                notebook[dtc]['Содержание заметки'] = '-'

    elif command == '6': # Помощь -6
        print(txt6)  
    elif command == '4': # Удаление данных -4
        notetitle = input('Ведите название заметки подлежащий удалению: - ')
        for key in notebook:
            if notetitle == notebook[key]['Название заметки']:
                del notebook[key]
                print('Заметка с названием - ', notetitle, ' найдена и удалена.')
                break
        else:
            print('Заметки с таким названием нет')   
    elif command == '7': # Сохранение данных -7
        save(notebook) 
    elif command == '8': # Загрузка данных -8
        notebook = load()
    elif command == '9': # Поиск данных -9
        num = checkInputNumber(txt7, txt2, 0, 2)
        while int(num) <= 2:
            if num == '1':
                print('Возможные варианты...\n')
                for key in notebook:
                    ekey = extractDateFromText(key)
                    print('\t', ekey.year, '.', ekey.month, '.', ekey.day, '.', notebook[key]['Название заметки'])
                print('...')
                nummatching = False
                year = int(checkInputNumber('Для уточнения введите год создания заметки(из перечисленных выше): - ', txt2, 1, 9999))
                while nummatching == False:
                    for key in notebook:
                        ekey = extractDateFromText(key)
                        if year == int(ekey.year):
                            nummatching = True
                    if nummatching == False:
                        year = input('Введены неверные данные, введите год создания заметки(из перечисленных выше): - ')
                print('Возможные варианты...\n')
                for key in notebook:
                    ekey = extractDateFromText(key)
                    if year == int(ekey.year):
                        print('\t', ekey.year, '.', ekey.month, '.', ekey.day, '.', notebook[key]['Название заметки'])
                print('...')
                chek = 0
                nummatching = False
                month = int(checkInputNumber('Для уточнения введите месяц создания заметки(из перечисленных выше): - ', txt2, 1, 12))
                while nummatching == False:
                    for key in notebook:
                        ekey = extractDateFromText(key)
                        if month == int(ekey.month) and year == int(ekey.year):
                            nummatching = True
                    if nummatching == False:
                        month = input('Введены неверные данные, введите месяц создания заметки(из перечисленных выше): - ')
                print('Возможные варианты...\n')
                for key in notebook:
                    ekey = extractDateFromText(key)
                    if month == int(ekey.month) and year == int(ekey.year):
                        print('\t', ekey.year, '.', ekey.month, '.', ekey.day, '.', notebook[key]['Название заметки'])
                print('...')
                nummatching = False
                day = int(checkInputNumber('Для уточнения введите день создания заметки(из перечисленных выше): - ', txt2, 1, 31))
                while nummatching == False:
                    for key in notebook:
                        ekey = extractDateFromText(key)
                        if day == int(ekey.day) and month == int(ekey.month) and year == int(ekey.year):
                            chek = ekey.day
                            nummatching = True
                    if nummatching == False:
                        day = input('Введены неверные данные, введите день создания заметки(из перечисленных выше): - ')
                print('Возможные варианты...\n')
                for key in notebook:
                    ekey = extractDateFromText(key)
                    if day == int(ekey.day) and month == int(ekey.month) and year == int(ekey.year):
                        print('\t', ekey.year, '.', ekey.month, '.', ekey.day, '.', notebook[key]['Название заметки'])
                print('...')
                text_1 = 'Для уточнения введите название заметки: - '
                text_2 = 'Название заметки'
                notebook = searchAndCorrectionData(text_1, text_2, notebook)
                num = checkInputNumber(txt7, txt2, 0, 2)
            elif num == '2':
                text_1 = 'Введите название заметки: - '
                text_2 = 'Название заметки'
                notebook = searchAndCorrectionData(text_1, text_2, notebook)
                num = checkInputNumber(txt7, txt2, 0, 2)
            elif num == '0':
                break