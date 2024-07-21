N1, N2, N3, N4 = map(float, input().split())

# Cálculo da média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

# Saída da média inicial (formatada com 1 casa decimal)
print(f"Media: {media:.1f}")

# Verificação da situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    # Caso de exame
    print("Aluno em exame.")
    exame = float(input("Nota do exame:"))  # Lê a nota do exame
    print(f"Nota do exame: {exame:.1f}")
    media_final = (media + exame) / 2  # Recálculo da média
    print(f"Media final: {media_final:.1f}")  

    # Verificação do resultado final após o exame
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
