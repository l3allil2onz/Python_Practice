# sum of list number
def getSumListNumbers(list_num):
    return sum(list_num)

print('\n----Sum of list number----')
print('Enter expected list length :')
while(True):
    try:
        strInput = input('  -> ')
        listLength = int(strInput)
        break
    except ValueError:
        print('[!] Invalid input. Please enter a valid integer.')
        
print('Enter your expected number in list :')
listNum = []
for number in range(listLength):
    while(True):
        try:
            strInput = input('  -> ')
            listNum.append(int(strInput))
            break
        except ValueError:
            print('[!] Invalid input. Please enter a valid integer.')
            
print('Sum number result = ',getSumListNumbers(listNum))
print('-----------END------------\n')