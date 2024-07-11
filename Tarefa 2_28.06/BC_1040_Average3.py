'''
N1, N2, N3, N4 = map(float, input().split())

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")

if media < 5.0:
    print ("Aluno reprovado.")

if media >= 5.0 and media <= 6.9:
    print ("Aluno em exame.")
    exame = float(input("Nota do exame: "))
    media_final = ((media + exame)/2)

    if media_final >= 5.0:
        print ("Aluno aprovado.") 
        print (f"Media final: {media_final:.1f}")

    else: 
        print("Aluno reprovado.")
'''

# Read the four scores
N1, N2, N3, N4 = map(float, input().split())

# Calculate the weighted average
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

# Print the initial average
#print(f"Media: {media:.1f}")

# Check the initial average and determine the student's status
if media >= 7.0:
    print("Aluno aprovado.")  # Approved
elif media < 5.0:
    print("Aluno reprovado.") # Reproved
else:  # 5.0 <= average <= 6.9
    #print("Aluno em exame.")  # In exam

    # Read the exam score
    exame = float(input())

    # Print the exam score
    print(f"Nota do exame: {exame:.1f}")

    # Recalculate the average with the exam score
    media_final = (media + exame) / 2

    # Print the final average and status
    print(f"Media final: {media_final:.1f}")
    if media_final >= 5.0:
        print("Aluno aprovado.")  # Approved
    else:
        print("Aluno reprovado.") # Reproved