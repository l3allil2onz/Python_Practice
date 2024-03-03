# get maximum number 
def getMaxValue(list_num):
    return max(list_num)

print('\n-------Get max value-------')
input = input('Enter list of numbers separated by (,): ')
input_list = input.split(',')
result = getMaxValue(input_list)
print('List = ', input_list)
print('Max value -> ', result)
print('------------END------------\n')