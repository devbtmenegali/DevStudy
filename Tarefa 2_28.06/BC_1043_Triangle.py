
A, B, C = map(float, input().split())

if (B + C) > A: 
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")

else:
    area = 0.5 * C * (A + B)  
    print(f"Area = {area:.1f}")