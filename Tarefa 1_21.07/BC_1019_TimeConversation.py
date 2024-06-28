#ATIVIDADE 1019 Time Conversation

seconds = int(input())

hours = seconds // 3600     
seconds %= 3600           
minutes = seconds // 60   
seconds %= 60                                  # %= é usado para atualizar o valor de uma variável calculando o resto da divisão da variável pelo valor à direita do operador e, em seguida, atribuindo esse resto de volta à variável.

print(f"{hours}:{minutes}:{seconds}")  