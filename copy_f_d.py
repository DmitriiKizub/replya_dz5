import os
import shutil
def copy(dir_file):
    if os.path.exists(f'{os.getcwd()}/{dir_file}'):
        if os.path.isfile(f'{os.getcwd()}/{dir_file}'):
            shutil.copy(f'{os.getcwd()}/{dir_file}',
                            f'C:\\Users\\d.kizub\\PycharmProjects\\replya_dz5\\copy\\{dir_file}')
            print("*" * 15)
            print(f'Скопирован файл "{dir_file}"')
            print("*" * 15)
        elif os.path.isdir(f'{os.getcwd()}/{dir_file}'):
            if os.path.exists(f'{os.getcwd()}\\copy\\{dir_file}'):
                print("*" * 15)
                print('Папка уже существует')
                print("*" * 15)
            else:
                shutil.copytree(f'{os.getcwd()}/{dir_file}',
                                f'C:\\Users\\d.kizub\\PycharmProjects\\replya_dz5\\copy\\{dir_file}')
                print("*" * 15)
                print(f'Папка "{dir_file}" скопирована')
                print("*" * 15)
    else:
        print("Проверьте название файла\папки")
