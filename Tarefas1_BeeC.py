# ATIVIDADE 2 BEECROWD

#A = int(input("A:"))
#B = int(input("B:"))
#X = A + B

#print(f"x = {X}\n")

#ATIVIDADE 1018 BEECROWD --> não funcionou.

value = int(input())
banknotes = [100, 50, 20, 10, 5, 2, 1]

print(value)

for notes in banknotes:                                      # Itera sobre as notas disponíveis
    quantidade = value // notes                              # Calcula quantas notas deste valor são necessárias,o operador // é chamado de divisão inteira ou floor division. Ele realiza a divisão entre dois números e retorna o quociente inteiro
    quantidade > 0                                         # Se for necessário pelo menos uma nota, imprime a informação

    value %= notes

print(f"{quantidade} nota(s) de R$ {notes},00")             # Atualiza o valor restante após usar as notas deste valor

#ATIVIDADE 1019 BEECROWD

seconds = int(input())

hours = seconds // 3600     
seconds %= 3600           
minutes = seconds // 60   
seconds %= 60                                  # %= é usado para atualizar o valor de uma variável calculando o resto da divisão da variável pelo valor à direita do operador e, em seguida, atribuindo esse resto de volta à variável.

print(f"{hours}:{minutes:02d}:{seconds:02d}")  #:02d garante que minutos e segundos sejam exibidos com dois dígitos, adicionando um zero à esquerda


#ATIVIDADE 1020 BEECROWD

days = int(input())

year = days // 365 #days
days %= 365
month = days // 30 #days
days %= 30

print(f"{year} anos")
print(f"{month} meses")
print(f"{days} dias")


#ATIVIDADE 1021 - Banknotes and Coins



#ATIVIDADE 1035 -> Selection Test 1

A, B, C, D = map(int, input().split())

if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


# 1036 -> Bhaskara's Formula

# 1037 ->Interval