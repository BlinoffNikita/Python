from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные:\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Введите корректную команду")
        command = int(input('Введите число'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
            
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
        
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def search_data():
    print("По какому полю выполнить поиск?")
    search_field = input("1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n")
    print()
    search_value = None
    if search_field == "1":
        search_value = input("Введите фамилию для поиска: ")
        print()
    elif search_field == "2":
        search_value = input("Введите имя для поиска: ")
        print()
    elif search_field == "3":
        search_value = input("Введите номер для поиска: ")
        print()
    return search_field, search_value


def change_data(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print("Какое поле вы хотите изменить?")
    field = input("1 - Фамилия\n2 - Имя\n3 - Номер телефона\n")
    if field == "1":
        number_to_change[0] = input("Введите фамилию: ")
    elif field == "2":
        number_to_change[1] = input("Введите имя: ")
    elif field == "3":
        number_to_change[2] = input("Введите номер телефона: ")
    contact_list.append(number_to_change)
    with open(file_name, "w", encoding="utf-8") as file:
        for contact in contact_list:
            line = ' '.join(contact) + "\n"
            file.write(line)


def delete_data(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, "w", encoding="utf-8") as file:
        for contact in contact_list:
            line = ' '.join(contact) + "\n"
            file.write(line)


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines(): 
            contact_list.append(line.split())
    return contact_list


def search_to_modify(contact_list: list):
    search_field, search_value = search_data()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value: 
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1: 
        print("Найдено несколько контактов")
        for i in range(len(search_result)):
            print(f"{i + 1} - {search_result[i]}")
        num_count = int(input("Выберите номер контакта, который нужно изменить/удалить: "))
        return search_result[num_count - 1]
    else: 
        print("Контакт не найден")
    print()