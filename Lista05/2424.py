bolota = input().split()
x = int(bolota[0])
y = int(bolota[1])
if x < 0:
  print('fora')
elif x > 432:
  print('fora')
elif 0 <= x <= 432:
  if y < 0:
    print('fora')
  elif y > 468:
    print('fora')
  elif 0 <= y <= 468:
    print('dentro')
