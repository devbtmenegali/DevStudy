
#ATIVIDADE 1018 Banknotes

value = int(input())                                    

print(value)                                            

notes = [100, 50, 20, 10, 5, 2, 1]                                          # Lista de notas

for note in notes:                                                          # Itera sobre as cédulas
    quant = value // note                                                   # Calcula a quantidade desta cédula
    print(f"{quant} nota(s) de R$ {note:.2f}".replace(".", ","))            # # Imprime o resultado com vírgula
    value %= note                                                           # Atualiza o valor restante após usar esta cédula


#.replace(".", ","):
#Após formatar o valor da cédula com :.2f, esta parte do código substitui 
#todos os pontos (.) por vírgulas (,) na string resultante.
