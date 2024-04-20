'''Урок8 по работе с файлами'''
import csv
def phone_book ():
    print('МЕНЮ: 1-Поиск; 2-Добавить; 3-Удалить; 4-Изменить; ; 5-Вывести весь справочник; 0-Выход')
    comand=int(input('Введите команду необходимого действия:>'))
    if comand==0:
        exit()
    if comand==1:
        search()
    # if comand==2:
    #     delete()
    return comand
def search():
    print('Для выхода в МЕНЮ введите 0')
    s=input('Поисковый запрос:>')# поисковый запрос
    # print(type(s))
    if s.isdigit() and int(s)==0:# проверяем состоит ли запрос из цифр
        # if int(s)==0:
            phone_book()

    else:
        with open('phone_book.csv', 'r') as book:
            file_reader=csv.reader(book, delimiter = "*")
            # print(s in file_reader)
            for row in file_reader:
                if s in row:
                    print(*row)
                    search()
                # else:
            print(f'`{s}` не найдено')
            search()




# def add():
# def delete():
# def to_change():

phone_book()