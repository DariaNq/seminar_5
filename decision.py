from fanction import new_contact


def new_name():
    with open('phone_book.txt', 'a+') as file:
       file.write(f'{new_contact} \n')


def read_book():
    print("Ваша телефонная книга: \n")
    with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
        file.write(f'{phone_book.txt}\n')

