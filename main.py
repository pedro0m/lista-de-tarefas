list_task = list()

def showTask(list_task):
    if list_task == []:
        print('Your List Are Empty.')

    else:
        for n, t in enumerate(list_task):
            print(f'{n+1} - {t}')

def createTask(list_task):
    new_task = str(input('Write a New Task: '))
    list_task.append(new_task)

def completeTask(list_task):
    ask = int(input('1 - Complete Task\n2 - Return to Options' \
                    '\nWhat You Need?: '))
    
    if ask == 1:
        v = int(input('Enter a Number Task You Need Complete: '))
        list_task.pop(v-1)
        print(25 * '=')
        print('Your Task Are Complete')

    elif ask == 2:
        print(25 * '=')
        print('Coming Back...')

    else:
        print('Write Only Numbers of 1 at 3')

def firstOption(list_task):
    while True:
        print(25 * '=')
        ask = int(input('1 - Show All Tasks\n2 - Create New Task\n3 - Complete One Task\n4 - Exit The Program\nWhat You Need?: '))

        if ask == 1:
            print(25 * '=')
            showTask(list_task)

        elif ask == 2:
            print(25 * '=')
            createTask(list_task)

        elif ask == 3:
            if list_task == []:
                print(25 * '=')
                print('Your List Are Empty.')

            else:
                print(25 * '=')
                showTask(list_task)
                print(25 * '=')
                completeTask(list_task)

        elif ask == 4:
            print(25 * '=')
            print('Leaving Out...')
            break

        else:
            print(25 * '=')
            print('Write Only Numbers of 1 at 3')

firstOption(list_task)