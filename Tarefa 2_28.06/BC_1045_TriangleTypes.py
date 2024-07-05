'''
Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:

if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
'''

A, B, C = map(float,input().split())

if A >= B + C:
    print(f"NAO FORMA TRIANGULO")
if A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")
elif A**2 > B**2 + C**22:
    print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")
elif A == B == C:
    print(f"TRIANGULO EQUILATERO")
elif a == b and a != c or b == c and b != a or a == c and a != b:
    print("TRIANGULO ISOSCELES")


