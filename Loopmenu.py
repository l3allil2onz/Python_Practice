print('\n')
con = True

def ShowMenu():
    print('---Selectable Menu---')
    print('(1) Addition')
    print('(2) Subtraction')
    print('(3) Multiplication')
    print('(4) Division')
    print('(5) Exit')
    print('---------------------')

def SelectableMenu(number):
    match number:
        case 1:
            print('-> Addition')
        case 2:
            print('-> Subtraction')
        case 3:
            print('-> Multiplication')
        case 4:
            print('-> Division')
        case 5:
            print('-> Exit')
        case 666:
            return False
        case _:
            print('[!] You Enter Wrong Number!!!')
    print('\n')
    return True

while(con):
    ShowMenu()
    try:
        number = int(input('Enter menu number: '))
    except:
        print('[!] Please enter correctly integer.')

    con = SelectableMenu(number)

print('\n')