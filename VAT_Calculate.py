print('\n')
salary = float(input('Enter salary: '))
rate = 0.0

if salary < 15000:
    rate = 0.0
    print(salary,'(VAT 0%) =>',salary*rate,'฿')
elif salary >= 15001 and salary <= 30000:
    rate = 5.0 / 100
    print(salary,'(VAT 5%) =>',salary*rate,'฿')
elif salary > 30000:
    rate = 10.0 / 100
    print(salary,'(VAT 10%) =>',salary*rate,'฿')

print('\n')