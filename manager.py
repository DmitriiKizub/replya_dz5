import os
import sys
# Меню
while True:
    print(
        '1. Создать папку \n2. Удалить (файл\папку)\n3. Копировать (файл\папку)\n4. Просмотр содержимого рабочей директории\n5. Посмотреть только папки\n6. Просмотреть только файлы\n7. Просмотр информации об операционной системе\n8. Создатель программы\n9. Играть в викторину\n10. Мой банковский счет\n11. смена рабочей директории (*необязательный пункт)\n12. Выход')
    chose = input('Выбирите пункт меню: ')

    if chose == '1':
        name_new_dir = input('Введите название папки: ')
        os.mkdir(name_new_dir)

    elif chose == '2':
        name_del_dir = input('Введите название удаления (файла\папкb): ')
        from del_file_dir import del_f_d
        del_f_d(name_del_dir)

    elif chose == '3':
        name_copy_dir = input('Введите название копируемого (файла\папки): ')
        from copy_f_d import copy
        copy(name_copy_dir)
    elif chose == '4':
        print(os.listdir())
    elif chose == '5':
        from look_file import show_dir
        show_dir()
    elif chose == '6':
        from look_file import show_file
        show_file()
    elif chose == '7':
        print("*" * 15)
        print(sys.platform)
        print("*" * 15)
    elif chose == '8':
        from author import author_name
        print(author_name())
    elif chose == '12':
        break










