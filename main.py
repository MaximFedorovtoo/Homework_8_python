from functions import *



def main():
    print(f"'add' добавить контакт\n"
          "'show' посмотреть справочник\n"
          "'find' поиск контакта \n"
          "'del' удалить контакт\n"
          "'edit' редактировать\n"
          "'stop' завершение программы")
    
    i = True
    while i == True:
        comand = input('Введите команду ')   
        match comand:
            case 'add': add_contact()
            case "find": search_contact()
            case "show": show_phonebook()
            case "edit": edit_contact()
            case "del": del_contact()
            case "stop": i = False
            case _:
                print('нет такой команды')

        # if comand == 'add': add_contact()
        # elif comand == 'find': search_contact()
        # elif comand == 'show': show_phonebook()
        # elif comand == 'edit': edit_contact()
        # elif comand == 'del': del_contact()
        # elif comand == 'stop': i = False
    

if __name__ == '__main__':
    main()