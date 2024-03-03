# get all sum of product prices
def getSumProductPrices(products: dict):
    return sum(products.values())

print('\n----Sum all of product prices----')
print('Enter your expected list length :')
while(True):
    try:
        strInput = input('  -> ')
        dicLength = int(strInput)
        break
    except ValueError:
        print('[!] Invalid input. Please enter a valid integer.')
        
print('-----------Product List----------')
dicProduct = {}
for i in range(dicLength):
    keyInput = input('Enter your product (' + str(i+1) + ') name :\n  -> ')
    while(True):
        try:
            priceInput = float(
                input('Enter your (' + keyInput + ') price :\n  -> '))
            dicProduct[keyInput] = priceInput
            break
        except ValueError:
            print('[!] Invalid input. Please enter a valid float.')
    print('---------------------------------')
            
print('---------------------------------')
result = getSumProductPrices(dicProduct)
print('Products = ', dicProduct)
print('Total Prices -> ', result)
print('---------------END---------------\n')