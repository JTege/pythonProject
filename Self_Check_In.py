# Variables

name = 'Jamir Ntege'  # str
position_number = 12  # int
rating = 45.5  # float
# print(name, position_number, rating)
print('Name: ' + name + ',', 'Position Number: ' + str(position_number) + ' &', 'Rating: ' + str(rating))

# Receiving Input

name = input('Enter your name? ')
print('Thank you ' + name)

# Conversions
# str
# num
# float
# booleans

birth_year = input('Enter your birth year: ')
age = 2024 - int(birth_year)
print('Age: ', str(age))

# first = float(10.1)
# second = float(20 + 20)
# print(first + second)

first = input('Enter position number: ')
second = input('Enter rating: ')
# sum = int(first) + int(second)
sum = float(first) + float(second)
print(sum)
# print("Sum: " + str(sum))

# first = float(input('Enter position number: '))
# second = float(input('Enter rating: '))
# sum = first + second
# print(sum)

temperature = float(input('Enter temperature? '))
if temperature > 38:  # if + condition
    print('Patient needs to request COVID test')
elif temperature < 28:  # terminate the block
    print('High risk of Hypothermia')  # in between 28 and 38
else:
    print('Normal Temperature - COVID test not needed')

weight = float(input('weight: '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == 'K':  # case-sensitive language
    converted = weight / 2.20
    print('weight in Lbs: ' + str(round(converted, 4)))
else:
    converted = weight * 2.20
    print('Weight in Kgs: ' + str(round(converted, 4)))
