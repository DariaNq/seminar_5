from fanction import name_data, phone_data, surname_data


def new_contact():
    name = name_data()
    phone = phone_data()
    surname = surname_data()
    with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}: {surname}: {phone}\n')


def read_book():
    print('Ваша телефонная книга: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
