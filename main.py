'''Урок8 по работе с файлами'''
import csv

def search():
    print('Для выхода в МЕНЮ введите 0')
    s=input('Поисковый запрос:>').lower()# поисковый запрос
    exit_menu(s)
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        counter=0
        for row in file_reader:
            if s in row:
                print(*row)
                counter+=1
        if counter==0:
            print(f'`{s}` не найдено')
        search()

def exit_menu(s):
    if s.isdigit() and int(s)==0:# проверяем состоит ли запрос из цифр
        phone_book()

def phone_book ():
    print('МЕНЮ: 1-Поиск; 2-Добавить; 3-Удалить; 4-Изменить; 5-Вывести весь справочник; 0-Выход')
    comand=int(input('Введите команду необходимого действия:>'))
    if comand==0:
        exit()
    if comand==1:
        search()
    if comand==2:
        add()
    if comand==3:
        delete()
    if comand==4:
        to_change()


def add():
    print('Для выхода в МЕНЮ введите 0. Введите Фамилию, Имя, Отчество, Телефон')
    new_id = []
    f=input('Введите Фамилию:>')
    exit_menu(f)
    new_id.append(f.lower())
    f = input('Введите Имя:>')
    exit_menu(f)
    new_id.append(f.lower())
    f = input('Введите Отчество:>')
    exit_menu(f)
    new_id.append(f.lower())
    f = input('Введите Телефон:>')
    exit_menu(f)
    new_id.append(f.lower())
    with open('phone_book.csv', 'r') as book:
        file_reader = csv.reader(book, delimiter="*")
        for row in file_reader:
            if new_id==row:
                x=input('Такая запись существует, записать еще раз? `да` `нет`:>')
                exit_menu(x)
                if x=='да':
                    book=open('phone_book.csv', 'a')
                    file_writer = csv.writer(book, delimiter="*")
                    file_writer.writerow(new_id)
                    book.close()
                    phone_book()
                if x=='нет':
                    phone_book()
        if new_id!=row:
            print(f'Вы ввели {new_id}')
            x=input('Сохранить? `да` `нет`:>')
            exit_menu(x)
            if x == 'да':
                book = open('phone_book.csv', 'a')
                file_writer = csv.writer(book, delimiter="*")
                file_writer.writerow(new_id)
                book.close()
                phone_book()
            if x == 'нет':
                phone_book()
def delete():
    print('Для выхода в МЕНЮ введите 0. Введите Фамилию, Имя, Отчество, Телефон записи которую надо удалить')
    del_id = []
    f = input('Введите Фамилию:>')
    exit_menu(f)
    del_id.append(f.lower())
    f = input('Введите Имя:>')
    exit_menu(f)
    del_id.append(f.lower())
    f = input('Введите Отчество:>')
    exit_menu(f)
    del_id.append(f.lower())
    f = input('Введите Телефон:>')
    exit_menu(f)
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
            delete()
    x=input('Укажите номер строки которую необходимо удалить:>')
    exit_menu(x)
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
    phone_book()

def to_change():
    print('Для выхода в МЕНЮ введите 0')
    s = input('Поисковый запрос:>').lower()  # поисковый запрос
    exit_menu(s)
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
            to_change()
    x = input('Укажите номер строки которую необходимо заменить:>')
    exit_menu(x)
    del_row = rows.pop(int(x) - 1)
    change_id = []
    f = input('Введите Фамилию:>')
    exit_menu(f)
    change_id.append(f.lower())
    f = input('Введите Имя:>')
    exit_menu(f)
    change_id.append(f.lower())
    f = input('Введите Отчество:>')
    exit_menu(f)
    change_id.append(f.lower())
    f = input('Введите Телефон:>')
    exit_menu(f)
    change_id.append(f.lower())
    rows.insert(int(x) - 1, change_id)
    book = open('phone_book.csv', 'w+')
    file_writer = csv.writer(book, delimiter='*')
    file_writer.writerows(rows)
    book.close()
    print(f'Запись {del_row} заменена на {change_id}')
    phone_book()


phone_book()