import csv

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


