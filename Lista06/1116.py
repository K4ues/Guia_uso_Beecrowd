x = int(input())
for i in range(x):
  number = input()
  separation = number.split()
  a = int(separation[0])
  b = int(separation[1])
  if b == 0:
    print('divisao impossivel')
  else:
    formule = a/b
    print(f'{formule}')
