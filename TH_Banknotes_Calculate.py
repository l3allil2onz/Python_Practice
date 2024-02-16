print('\n')
print('-------TH_Banknotes_Calculate-------')
money = input('Enter your money: ')

totalMoney = int(money)
B1000 = 1000
B500 = 500
B100 = 100
B20 = 20

print('--------------Display--------------')
print('Total money: ',totalMoney)
print('-----------------------------------')
floorB1000 = totalMoney
floorB1000 //= B1000
totalMoney %= B1000 
print('B1000 amount: ',floorB1000,' bill')
print('Remain -> ',totalMoney)
print('-----------------------------------')
floorB500 = totalMoney
floorB500 //= B500
totalMoney %= B500
print('B500 amount: ',floorB500,' bill')
print('Remain -> ',totalMoney)
print('-----------------------------------')
floorB100 = totalMoney
floorB100 //= B100
totalMoney %= B100
print('B100 amount: ',floorB100,' bill')
print('Remain -> ',totalMoney)
print('-----------------------------------')
floorB20 = totalMoney
floorB20 //= B20
totalMoney %= B20
print('B20 amount: ',floorB20,' bill')
print('Remain -> ',totalMoney)
print('--------------Summary--------------')
print('Total money:',money)
print('Banknotes: ')
print('-> B1000  = ',floorB1000,' bill')
print('-> B500   = ',floorB500,' bill')
print('-> B100   = ',floorB100,' bill')
print('-> B20    = ',floorB20,' bill')
print('-> Remain = ',totalMoney,' coin')

print('\n')