# Длина кольцевой автодороги
s0 = 109
v = int(input('ВВедите скорость мотоциклиста, км/ч    '))
t = int(input('ВВедите длительность поездки мотоциклиста, ч    '))
# point - отметка остановки мотоциклиста
point = (v * t) - ((v * t) // s0) * s0
print(point)