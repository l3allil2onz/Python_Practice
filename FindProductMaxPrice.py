# get product has maximum price
def getProductMaxPrice(products):
    max_price = max(products.values())

    for product, price in products.items():
        if price == max_price:
            return product

print('\n---------Get product has maximum price---------')
input_dic = {}
product_keys = []
product_values = []
while True:
    print("\n-----------------Your Input--------------------")
    input_product_keys = input('Enter product key: ')

    if input_product_keys.lower() == '_stop':
        break
    product_keys.append(input_product_keys)

    input_product_values = input('Enter price value: ')

    if input_product_values.lower() == '_stop':
        print('[!] Please enter the last value input before')
        input_product_values = input('[!] Enter value: ')
        product_values.append(input_product_values)
        break
    product_values.append(input_product_values)

    print("---------------Your Container------------------")
    print("Your product key -> ", product_keys)
    print("Your product value -> ", product_values)
    print("-----------------------------------------------")
    print("[?] Enter '_stop' to exit input product\n")

    input_dic = dict(zip(product_keys, product_values))

if input_dic != {}:
    result = getProductMaxPrice(input_dic)
    print("\n-------------------Summary---------------------")
    print('Products = ', input_dic)
    print('Product has max price -> ', result)
    print('---------------------END-----------------------\n')