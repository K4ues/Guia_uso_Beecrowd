m = 0
pos = 0
for x in range(100):
  n = int(input())
  if n>m:
    m = n
    pos = x

print(m)
print(pos+1)
