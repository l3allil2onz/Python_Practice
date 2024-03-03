# get odd numbers
def getOddNumbers(list_num):
    list_odd = []

    for n in list_num:
        if int(n) % 2 != 0:
            list_odd.append(n)

    return list_odd

input_num = input('Enter list of numbers separated by (,): ')
input_list = input_num.split(',')
print('Your list numbers', input_list)
result = getOddNumbers(input_list)

print('\n-----Get odd numbers------')
print('List = ', input_list)
print('Total odd numbers -> ', result)
print('-----------END------------\n')