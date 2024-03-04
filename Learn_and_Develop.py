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

# strings

i = '*'
print(i*150)

course = ("Python for Jams' Learning")  # str - Object
print(course.upper())  # method uppercase
print(course.find('y'))  # index of characters (012345...)
print(course.find('Jams'))  # index of 'sequence of characters'
print(course.replace('for', '4'))  # method replace
print('Learning' in course)  # Boolean

# Arithmetic Operators

print(20 / 3)  # divide
print(20 // 3)  # returns integer or whole number
print(20 % 3)  # reduce to the lowest terms
print(10 ** 3)  # 10 to the power of 3

x = 10
# x = x + 3 # enhancement v1
x += 3  # enhancement v2
print(x)

# Operator Precedence

y = (24 + 4) * 2
print(y)

# Comparison Operator

# T = 3 > 2 # boolean expression
# T = 30 >= 10
# T = 20 <= 40
# T = 60 == 60 # Equal
T = 20 != 21  # Not Equal
print(T)  # boolean

# Logical Operators

price = 25
# print(price > 10 and price < 30) # and
# print(price > 20 or price < 30) # or
print(not price > 20)

i = '*'
print(i*150)

# If statement

temperature = float(input('Enter temperature? '))
if temperature > 38:  # if + condition
    print('Patient needs to request COVID test')
elif temperature < 28:  # terminate the block
    print('High risk of Hypothermia')  # in between 28 and 38
else:
    print('Normal Temperature - COVID test not needed')

weight = float(input('weight: '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == 'K':  # case sensitive language
    converted = weight / 2.20
    print('weight in Lbs: ' + str(round(converted, 4)))
else:
    converted = weight * 2.20
    print('Weight in Kgs: ' + str(round(converted, 4)))  # Not achieving the round result to develop further

i = '*'
print(i*150)

# While loops

i = 1
while i <= 10:
    print(i)
    i = i + 1  # i incremented by 1

i = 1
while i <= 10:
    print(i * '*')  # Multiplication can be accepted with a num & str
    i = i + 1

# List

ward = ['Sun', 'Moon', 'Earth', 'Sky', 'Seas', 'Land']
print(ward)

ward = ['Sun', 'Moon', 'Earth', 'Sky', 'Seas', 'Land']
print(ward[0])  # index to return results

ward = ['Sun', 'Moon', 'Earth', 'Sky', 'Seas', 'Land']
print(ward[-1])  # returns last element of the index

ward = ['Sun', 'Moon', 'Earth', 'Sky', 'Seas', 'Land']
print(ward[-2])  # returns second last element of the index

ward = ['Sun', 'Moon', 'Earth', 'Sky', 'Seas', 'Land']
ward[4] = 'Ocean'
print(ward)

ward = ['Sun', 'Moon', 'Earth', 'Sky', 'Seas', 'Land']
ward[4] = 'Ocean'
print(ward[0:5])  # start index excluding the end index - does not modify the original list - returns a new list

# List Methods

waiting_positions = [1, 2, 3, 4, 5]
waiting_positions.append(6)  # add to a new element
print(waiting_positions)

waiting_positions = [1, 2, 3, 4, 5]
waiting_positions.insert(0, -1)  # insert any type of object - str, boolean, int, etc.
print(waiting_positions)

waiting_positions = [1, 2, 3, 4, 5]
waiting_positions.remove(5)
print(waiting_positions)

waiting_positions = [1, 2, 3, 4, 5]
waiting_positions.clear()
print(waiting_positions)

waiting_positions = [1, 2, 3, 4, 5]
print(3 in waiting_positions)  # return boolean value

waiting_positions = [1, 2, 3, 4, 5]
print(len(waiting_positions))

# For loops

performance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in performance:  # print each item on a separate line
    print(item)

performance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in performance:  # print each item on a separate line
    print(item)

H = 0
while H < len(performance):
    print(performance[H])
    H = H + 1  # increment H + 1

# The range () Function

performance = range(10)
print(performance)

performance = range(0, 10)  # first number is starting value and last number is excluding the last value
for number in performance:
    print(number)

performance = range(0, 10, 2)  # third number is a step - to be skipped or as a jump
for number in performance:
    print(number)

for performance in range(10):  # No variable required to return
    print(performance)

# [] to define a list and () to define a tuple - use a tuple if list does not need to be modified.

i = '*'
print(i*150)
