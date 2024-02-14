import os

def read_file():
    '''this function is for reading the content of files'''
    pat = input('please enter path name: ')
    try:
        with open(pat, 'r') as r:
            print(r.read())
    except FileNotFoundError:
        print('file not found')
        read_file()
    except PermissionError:
        print(os.listdir(pat))


def remove():
    ''' this function is for deleting the entred directory'''
    pat = input('please enter path name: ')
    try:
        os.remove(path=pat)
        return 'remove successful'
    except FileNotFoundError:
        print('file not found')
        remove()
    except PermissionError: 
        try:
            os.removedirs(pat)
            return 'remove successful'
        except OSError:
            print('directory is not empty')
            remove()


def rename():
    ''' this function is used to change the name of the entered directory '''
    try:
        pat = input('please enter path: ')
        new = input('please enter new name: ')
        os.rename(pat, new)
        return 'rename successful'
    except FileNotFoundError:
        print('file not found!')
        rename()


def copy():
    '''this function is used to copy the text file'''
    try:
        pat = input('please enter path: ')
        new = input('please enter new file name: ')
        with open(pat, 'r') as r:
            reader = r.read()
            with open(new, 'w') as w:
                writer = w.write(reader)
    except PermissionError:
        'path is not file!!'


def dir_list():
    '''this function is used to view the list of files in the entered directory'''
    try:
        pat = input('please enter path: ')
        return print(os.listdir(pat))
    except FileNotFoundError:
        print('file not found!')
        dir_list()


def move():
    '''this function is used to moveing the files '''
    try:
        pat = input('please enter path: ')
        new = input('please enter new path: ')
        os.replace(pat, new)
    except FileNotFoundError:
        print('file not found!')
        move()


def search():
    '''This function searches for a text in the file'''
    pat = input("please enter path: ")
    txt = input("please enter txt: ").lower()
    try:
        with open(pat, 'r') as r:
            reader = r.read()
            if txt in reader.lower():
                print('yes')
            else:
                print('no')
    except FileNotFoundError:
        print('file not found!!')
        search()


def count():
    '''This function is for calculating the number of characters in the file'''
    pat = input('please enter path: ')
    try:
        with open(pat, 'r') as r:
            reader = r.read()
            j = 1
            for i in reader:
                j += 1
            print('count of characters:',j)
    except FileNotFoundError:
        print('file not found!!')
        count()

while True:
    print('your directory: ',os.getcwd())
    print('''
    1) for reading the content of files Enter "read"
    2) for deleting the directory Enter "remove"
    3) for renameing the path Enter "rename"
    4) for copy txt file Enter "copy"
    5) for view the list of files in the directory Enter "dir list"
    6) for moveing the files Enter "move"
    7) for searching txt in file Enter "search"
    8) for calculating the number of characters in the file Enter "count"
    9) for Ending Enter "end"''')
    inp = input('please enter your Command: ').lower()
    if inp == 'read' or inp == '1':
        read_file()
    elif inp == 'remove' or inp == '2':
        remove()
    elif inp == 'rename' or inp == '3':
        rename()
    elif inp == 'copy' or inp == '4':
        copy()
    elif inp == 'dir list' or inp == '5':
        dir_list()
    elif inp == 'move' or inp == '6':
        move()
    elif inp == 'search' or inp == '7':
        search()
    elif inp == 'count' or inp == '8':
        count()
    elif inp == 'end' or inp == '9':
        break
    else:
        continue

