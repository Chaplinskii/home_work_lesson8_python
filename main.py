'''Урок8 по работе с файлами'''
import csv

def search():
    print('Для выхода в МЕНЮ введите 0')
    s=input('Поисковый запрос:>')# поисковый запрос
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





# def delete():
# def to_change():



phone_book()