import csv

book= open('phone_book.csv', 'r')
file_reader = csv.reader(book, delimiter="*")
rows=[]
for row in file_reader:

    rows.append(row)
book.close()
print(rows)
print(rows.pop(1))
print(rows)
book=open('phone_book.csv', 'w+')
file_writer=csv.writer(book, delimiter='*')
# file_writer
file_writer.writerows(rows)
book.close()


print(file_reader.line_num)