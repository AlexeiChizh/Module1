x1 = int(input('Введите координату ладьи от 1 до 8 по горизонтали:   '))
y1 = int(input('Введите координату ладьи от 1 до 8 по вертикали:   '))
x2 = int(input('Введите новую координату ладьи от 1 до 8 по горизонтали:   '))
y2 = int(input('Введите новую координату ладьи от 1 до 8 по вертикали:   '))
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
