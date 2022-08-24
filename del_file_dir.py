import os
def del_f_d(name):
        if os.path.isfile(f'{os.getcwd()}/{name}'):
            os.remove(name)
        elif os.path.isdir(f'{os.getcwd()}/{name}'):
            os.rmdir(name)
        else:
            print("*"*15)
            print(f'Данный каталог отсутствует')
            print("*"*15)
