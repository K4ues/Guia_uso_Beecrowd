dotone = input().split()
pont_x = float(dotone[0])
pont_y = float(dotone[1])
dottwo = input().split()
pont_xb = float(dottwo[0])
pont_yb = float(dottwo[1])
formula = ((pont_xb - pont_x) ** 2 + (pont_yb - pont_y) ** 2) ** 0.5
print(f'{formula:.4f}')
