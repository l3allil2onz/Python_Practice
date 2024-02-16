print('\n')
print('-----------BMI_CALCULATE-----------')
weight = float(input('Enter weight(kg): '))
height = float(input('Enter height(cm): ')) / 100
print('-----------------------------------')
print('weight = ',weight,' kg.')
print('height = ',height,' m.')
bmi = round(weight/(height*2),1)
print('bmi(h/(w*2)) = ',bmi)
print('-----------------------------------')
if bmi < 18.5:
    print('-> ผอม')
elif bmi <= 18.5 and bmi < 24.9:
    print('-> น้ำหนัก ปกติ')
elif bmi <= 24.9 and bmi < 29.9:
    print('-> น้ำหนัก เกิน')
elif bmi > 30.0:
    print('-> อ้วน')
else:
    print('err')

print('\n')