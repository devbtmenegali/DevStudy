# ATIVIDADE 1012 Area

#map() -> ferramenta que permite aplicar uma determinada função a cada elemento de um 
#objeto iterável (como uma lista, tupla ou conjunto) e retorna um novo objeto iterador 
#com os resultados.

A, B, C = map(float,input().split())
pi = 3.14159

triangle = (A * C) / 2
circle = (C ** 2) * pi
trapezium = ((A + B) * C) / 2
square = B ** 2
rectangle = A * B

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
