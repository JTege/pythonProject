i = '*'
print(i*150)


weight = float(input('weight: '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == 'K':  # case-sensitive language - requires fix
    converted = weight / 2.20
    print('weight in Lbs: ' + str(int(round(converted, 4))))
else:
    converted = weight * 2.20
    print('Weight in Kgs: ' + str(int(round(converted, 4))))

i = '*'
print(i*150)

# while loop

secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Win')
        break
else:
    print('fail')  # End of while loop

i = '*'
print(i*150)

# for item in range(10):  # for loop - be list, string, object e.g. Range function
#    print(item)

# for item in range(1, 10):
#    print(item)

for numbers in range(1, 10, 2):  # for loop - can be list, string, object e.g. Range function - (3rd num is a step)
    print(numbers)

i = '*'
print(i*150)

prices = [40, 60, 80]
total = 0
for amount in prices:
    total = total + amount
print(f'Total: {total}')

i = '*'
print(i*150)

# tuple
positions = ('First', 'Second', 'Third')
x, y, z = positions
print(x)
print(y)
print(z)

i = '*'
print(i*150)

# Dictionaries # value can be a string, int, boolean etc.

patients = {
    'patient_1': 'Jamir Ntege',
    'patient_2': 'Ntege Jamir',
    'patient_1_age': 95,
    'patient_2_age': 100
}
print(patients.get('patient_1'))  # get method - to pass a key that doesn't exist + spelling to avoid error msg
print(patients.get('patient_1_age'))
print(patients.get('patient_2'))
print(patients.get('patient_2_age'))
