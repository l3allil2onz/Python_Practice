print('\n')
print('-----Woring hrs calculate-----')
employee = [0] * 5
for i in range(5):
    employee[i] = float(input(f'Enter employee {i+1} working hrs : '))
    
print('----------Summary----------')
for i in range(5):
    if employee[i] > 30:
        print(f'Employee {i+1} Take more rest (-)')
    elif employee[i] < 10:
        print(f'Employee {i+1} Take more work (+)')

print('\n')