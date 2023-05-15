mexico = input().split()
A = float(mexico[0])
B = float(mexico[1])
C = float(mexico[2])

triangulo = A * C / 2
circle = C ** 2 * 3.14159
trapezio = (A + B) * C / 2
quadrado = B ** 2
retangulo = A * B

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circle:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
