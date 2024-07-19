#ATIVIDADE 1015 Distance Between Points

import math                                     #permite que você utilize as funções e constantes presentes no módulo math (funções matemáticas).

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   #sqrt é raiz quadrada.

print(f"{distance:.4f}")
