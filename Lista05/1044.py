number = input()
love = number.split(" ")
first = int(love[0])
second = int(love[1])
if first % second == 0:
  print('Sao Multiplos')
elif second % first == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
