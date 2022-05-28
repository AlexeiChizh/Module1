x = int(input('Введите любое целое число Х:   '))
y = int(input('Введите любое целое число Y:   '))
z = int(input('Введите любое целое число Z:   '))
if x == y == z:
	print(3)
elif x == y or y == z or x== z:
	print(2)
else:
	print(0)