i = '*'
print(i*150)


weight = float(input('weight: '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == 'K':  # case-sensitive language
    converted = weight / 2.20
    print('weight in Lbs: ' + str(round(converted, 4)))
else:
    converted = weight * 2.20
    print('Weight in Kgs: ' + str(round(converted, 4)))
