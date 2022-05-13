# BMI CALCULATOR
# This program calculates your body mass index and tell you how many kg you should gain or loose
# Made by Alessandro Silvestri

weight = int(input('Insert your weight in kg: '))
height = float(input('Insert your height in meter: '))
result = round(weight / height ** 2, 2)             # BMI formula
kg_to_fix = 0

# I calculate if the user is: underweight, normal, overweight or obese
print('---------------------')
print('result:', result)
if result < 18.4:
    print('Underweight')
elif 18.5 < result < 24.9:
    print('Normal range')
elif 25.0 < result < 29.9:
    print('Overweight')
elif result > 30.0:
    print('Obese')

# if the user is overweight I tell him how many kg he should loose
if result > 24.9:
    while result > 24.9:
        weight -= 1
        result = round((weight) / height ** 2, 2)
        kg_to_fix += 1
    print('You should loose: ', kg_to_fix, 'kg')

# if the user is too thin I tell him how many kg he should gain
if result < 18.5:
    while result < 18.5:
        weight += 1
        result = round((weight) / height ** 2, 2)
        kg_to_fix += 1
    print('You should gain:', kg_to_fix,'kg')

