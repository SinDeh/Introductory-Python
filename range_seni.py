# Ask for input from the user for their age
age = int(input())

# Check the age against multiple ranges and print corresponding labels
if 0 < age < 6:
    print('khordsal')
if 6 <= age < 10:
    print('koodak')
if 10 <= age < 14:
    print('nojavan')
if 14 <= age < 24:
    print('javan')
if 24 <= age < 40:
    print('bozorgsal')
if age >= 40:
    print('miansal')
