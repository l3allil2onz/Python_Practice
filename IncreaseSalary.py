# Increase employees salary by percent.
def IncreaseSalary(employees: dict,percent: float):
    new_salary_list = {}
    new_name = []
    new_salary = []
    rate = 1 + (percent/100)
    for name, salary in employees.items():
        new_name.append(name)
        new_salary.append(round(float(salary) * rate, 1))
    new_salary_list = dict(zip(new_name, new_salary))
    return new_salary_list

print('\n---------------Increase Salary-----------------')
input_dic = {}
employees_name_keys = []
employees_salary_values = []
percent = 10
while True:
    print("\n-----------------Your Input--------------------")
    input_employees_keys = input('Enter employees name: ')

    if input_employees_keys.lower() == '_stop':
        break
    employees_name_keys.append(input_employees_keys)

    input_employees_values = input('Enter employees salary: ')

    if input_employees_values.lower() == '_stop':
        print('[!] Please enter the last value input before')
        input_employees_values = input('[!] Enter value: ')
        employees_salary_values.append(input_employees_values)
        break
    employees_salary_values.append(input_employees_values)

    print("---------------Your Container------------------")
    print("Your employees name   -> ", employees_name_keys)
    print("Your employees salary -> ", employees_salary_values)
    print("-----------------------------------------------")
    print("[?] Enter '_stop' to exit input employees data\n")

    input_dic = dict(
        zip(employees_name_keys, employees_salary_values)
    )

if input_dic != {}:
    result = IncreaseSalary(input_dic,percent)
    print("\n-----------------Summary---------------------")
    print('Container = ', input_dic)
    print('After Increase Salary -> ')
    for index, (key, val) in enumerate(result.items()):
        print(f'    -> Employees [{index+1}] name: {key} | salary: {val}')
    print('---------------------END-----------------------\n')