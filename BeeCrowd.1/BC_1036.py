
def Bhaskaras_Formula():

    import math

    A, B, C = map(float,input().split())
    
    discriminant = B**2 - 4 * A * C

    if A == 0 or discriminant < 0:
        print("Impossivel calcular")
    else:
        R1 = (-B + math.sqrt(discriminant)) / (2 * A)
        R2 = (-B - math.sqrt(discriminant)) / (2 * A)

        print(f"R1 = {R1:.5f}")
        print(f"R2 = {R2:.5f}")

Bhaskaras_Formula()