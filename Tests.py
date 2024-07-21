# Get side lengths
while True:
    try:
        A = float(input("Enter side A: "))
        B = float(input("Enter side B: "))
        C = float(input("Enter side C: "))

        if A <= 0 or B <= 0 or C <= 0:
            raise ValueError("Side lengths must be positive.")

        break  # Sai do loop se todas as entradas forem válidas
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter positive numerical values for the sides.")

# Sort sides in descending order
sides = [A, B, C]
sides.sort(reverse=True)
A, B, C = sides

# Triangle Inequality Theorem (Check if a triangle is possible)
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Classify the triangle based on its angles and sides
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
    else:
        print("TRIANGULO ESCALENO")  # Adiciona a classificação de triângulo escaleno
