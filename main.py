'''Урок8 по работе с файлами'''
import csv

def search():
    print('Для выхода в МЕНЮ введите 0')
    s=input('Поисковый запрос:>').lower()# поисковый запрос
    if exit_menu(s):
        return phone_book()
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        counter=0
        for row in file_reader:
            if s in row:
                print(*row)
                counter+=1
        if counter==0:
            print(f'`{s}` не найдено')
        return search()
def add():
    print('Для выхода в МЕНЮ введите 0. Введите Фамилию, Имя, Отчество, Телефон')
    new_id = []
    f=input('Введите Фамилию:>')
    if exit_menu(f):
        return phone_book()
    new_id.append(f.lower())
    f = input('Введите Имя:>')
    if exit_menu(f):
        return phone_book()
    new_id.append(f.lower())
    f = input('Введите Отчество:>')
    if exit_menu(f):
        return phone_book()
    new_id.append(f.lower())
    f = input('Введите Телефон:>')
    if exit_menu(f):
        return phone_book()
    new_id.append(f.lower())
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        for row in file_reader:
            if new_id==row:
                x=input('Такая запись существует, записать еще раз? `да` `нет`:>')
                if exit_menu(x):
                    return phone_book()
                if x=='да':
                    book=open('phone_book.csv', 'a')
                    file_writer = csv.writer(book, delimiter="*")
                    file_writer.writerow(new_id)
                    book.close()
                    return phone_book()
                if x=='нет':
                    return phone_book()
        if new_id!=row:
            print(f'Вы ввели {new_id}')
            x=input('Сохранить? `да` `нет`:>')
            if exit_menu(x):
                return phone_book()
            if x == 'да':
                book = open('phone_book.csv', 'a')
                file_writer = csv.writer(book, delimiter="*")
                file_writer.writerow(new_id)
                book.close()
                return phone_book()
            if x == 'нет':
                return phone_book()
def delete():
    print('Для выхода в МЕНЮ введите 0. Введите Фамилию, Имя, Отчество, Телефон записи которую надо удалить')
    del_id = []
    f = input('Введите Фамилию:>')
    if exit_menu(f):
        return phone_book()
    del_id.append(f.lower())
    f = input('Введите Имя:>')
    if exit_menu(f):
        return phone_book()
    del_id.append(f.lower())
    f = input('Введите Отчество:>')
    if exit_menu(f):
        return phone_book()
    del_id.append(f.lower())
    f = input('Введите Телефон:>')
    if exit_menu(f):
        return phone_book()
    del_id.append(f.lower())
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        counter=0
        number_row=0
        for row in file_reader:
            number_row+=1
            if del_id == row:
                print(f'{number_row}{row}')
                counter+=1
        if counter==0:
            print(f'`{del_id}` не найдено')
            return delete()
    x=input('Укажите номер строки которую необходимо удалить:>')
    if exit_menu(x):
        return phone_book()
    book = open('phone_book.csv', 'r')
    file_reader = csv.reader(book, delimiter="*")
    rows = []
    for row in file_reader:
        rows.append(row)
    book.close()
    print(f'Запись {rows.pop(int(x)-1)} удалена')
    book = open('phone_book.csv', 'w+')
    file_writer = csv.writer(book, delimiter='*')
    file_writer.writerows(rows)
    book.close()
    return phone_book()
def to_change():
    print('Для выхода в МЕНЮ введите 0')
    s = input('Поисковый запрос:>').lower()  # поисковый запрос
    if exit_menu(s):
        return phone_book()
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        counter = 0
        number_row = 0
        rows = []
        for row in file_reader:
            rows.append(row)
            number_row += 1
            if s in row:
                print(f'{number_row}{row}')
                counter += 1
        if counter == 0:
            print(f'`{s}` не найдено')
            return to_change()
    x = input('Укажите номер строки которую необходимо заменить:>')
    if exit_menu(x):
        return phone_book()
    del_row = rows.pop(int(x) - 1)
    change_id = []
    f = input('Введите Фамилию:>')
    if exit_menu(f):
        return phone_book()
    change_id.append(f.lower())
    f = input('Введите Имя:>')
    if exit_menu(f):
        return phone_book()
    change_id.append(f.lower())
    f = input('Введите Отчество:>')
    if exit_menu(f):
        return phone_book()
    change_id.append(f.lower())
    f = input('Введите Телефон:>')
    if exit_menu(f):
        return phone_book()
    change_id.append(f.lower())
    rows.insert(int(x) - 1, change_id)
    book = open('phone_book.csv', 'w+')
    file_writer = csv.writer(book, delimiter='*')
    file_writer.writerows(rows)
    book.close()
    print(f'Запись {del_row} заменена на {change_id}')
    return phone_book()
def print_book():
    number_row=0
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        for row in file_reader:
            number_row += 1
            print(f'{number_row}{row}')
    return phone_book()
def copy_row():
    s = input('Поисковый запрос:>').lower()  # поисковый запрос
    if exit_menu(s):
        return phone_book()
    number_row = 0
    rows = []
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        counter = 0
        for row in file_reader:
            number_row += 1
            rows.append(row)
            if s in row:
                print(f'{number_row}{row}')
                counter += 1
        if counter == 0:
            print(f'`{s}` не найдено')
    x = input('Введите номер строки которую необходимо скопировать:>')
    if exit_menu(x):
        return phone_book()
    copy_id = rows[int(x) - 1]
    # print(copy_id)
    book = open('phone_book_home_work.csv', 'a')
    file_writer = csv.writer(book, delimiter="*")
    file_writer.writerow(copy_id)
    book.close()
    print(f'Строка {copy_id} скопирована в фаил phone_book_home_work.csv')
    return phone_book()
def exit_menu(s):
    if s.isdigit() and int(s)==0:# проверяем состоит ли запрос из цифр
        return True
def phone_book ():
    print('МЕНЮ: 1-Поиск; 2-Добавить; 3-Удалить; 4-Изменить; 5-Вывести весь справочник; 6-Копирование строки; 0-Выход')
    comand=int(input('Введите команду необходимого действия:>'))
    if comand==0:
        exit()
    if comand==1:
        return search()
    if comand==2:
        return add()
    if comand==3:
        return delete()
    if comand==4:
        return to_change()
    if comand==5:
        return print_book()
    if comand==6:
        return copy_row()
    if comand>6:
        return phone_book()

phone_book()