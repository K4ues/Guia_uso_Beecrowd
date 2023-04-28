numbers = input()
separation = numbers.split(" ")
meters = int(separation[0])
size = int(separation[1])
equal = meters%size
print(f'{equal}')
