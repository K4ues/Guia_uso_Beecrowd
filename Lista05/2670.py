floor1 = int(input())
floor2 = int(input())
floor3 = int(input())

minutos1 = floor1 * 0 + floor2 * 2 + floor3 * 4
minutos2 = floor1 * 2 + floor2 * 0 + floor3 * 2
minutos3 = floor1 * 4 + floor2 * 2 + floor3 * 0

if minutos1 <= minutos2:
    answer = minutos1
else:
    answer = minutos2
if answer >= minutos3:
    answer = minutos3

print(f'{answer}')
