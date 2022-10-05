from decision import new_contact, read_book

book = input('Что вам требуется: \n0 - новый контакт\n1 - просмотр книги \n')

if book == "0":
    new_contact()
elif book == "1":
    read_book()
else:
    book != 1 and book != 0
    print("Введите корректное значение! ")    
    book = input('Что вам требуется: \n0 - новый контакт\n1 - просмотр книги \n')
