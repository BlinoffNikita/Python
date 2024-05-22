from logger import input_data, print_data, search_data, change_data, delete_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник!\n 1 - Найти контакт\n 2 - Добавить контакт\n 3 - Изменить контакт\n 4 - Удалить контакт\n 5 - Показать телефонный справочник\n 0 - Закончить работу\n")
    command = int(input('Выберите необходимую команду '))
    
    while command != 1 and command != 2 and command != 3 and command != 4 and command != 5 and command != 0:
        print("Введите корректную команду")
        command = int(input('Выберите необходимую команду '))
        
    if command ==1:
        search_data()
    elif command == 2:
        input_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()
    elif command == 5:
        print_data()
    elif command == 0:
        print(" Работа окончена\n До скорой встречи!")
    