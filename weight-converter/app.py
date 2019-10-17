# This script will convert the weight input by the user to the desire unit
# From Pounds to Kilos and vice-versa
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.lower() == 'l':
    converted = weight * 0.453592
    print(f'You are {converted.__round__(1)} kilograms')
elif unit.lower() == 'k':
    converted = weight * 2.20462
    print(f'You are {converted.__round__(1)} pounds')

