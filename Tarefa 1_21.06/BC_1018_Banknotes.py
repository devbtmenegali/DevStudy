
#ATIVIDADE 1018 Banknotes


value = int(input())                                    

print(value)                                            

notes = [100, 50, 20, 10, 5, 2, 1]                      # Lista de notas

for note in notes:                                      # Itera sobre as cédulas
    quant = value // note                               # Calcula a quantidade desta cédula
    print(f"{quant} nota(s) de R$ {note:.2f}".replace(".", ","))         # Imprime o resultado
    value %= note                                       # Atualiza o valor restante após usar esta cédula


   