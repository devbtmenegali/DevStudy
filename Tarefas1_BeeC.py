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

#ATIVIDADE 1021 - Banknotes and Coins


# 1036 -> Bhaskara's Formula

# 1037 ->Interval