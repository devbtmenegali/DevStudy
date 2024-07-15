N1, N2, N3, N4 = map(float, input().split())

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

if media >= 7.0:
    print("Aluno aprovado.")  
elif media < 5.0:
    print("Aluno reprovado.") 
else:  
    exame = float(input())
    media_final = (media + exame) / 2
    print(f"Media: {media:.1f}")
    print(f"Aluno em exame.")
    print(f"Nota do exame: {exame:.1f}")
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")
  
    else:
        print("Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")
 