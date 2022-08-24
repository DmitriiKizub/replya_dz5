import os
def show_file():
    resulte =[]
    for item in os.listdir():
        if os.path.isfile(item):
            resulte.append(item)
    print(resulte)

def show_dir():
    resulte = []
    for item in os.listdir():
        if os.path.isdir(item):
            resulte.append(item)
    print(resulte)
