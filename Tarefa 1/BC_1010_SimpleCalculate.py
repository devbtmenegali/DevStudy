# ATIVIDADE 1010 Simple Calculate


#split() -> Separador: Você pode indicar um caractere ou uma sequência de caracteres que servirá /
#como delimitador para dividir a string. Se nenhum separador for fornecido, a função dividirá a /
#string em espaços em branco (espaços, tabulações, novas linhas, etc.).  

product1_code, product1_units, product1_price = input().split()         
product2_code, product2_units, product2_price = input().split()
total1 = int(product1_units) * float(product1_price)
total2 = int(product2_units) * float(product2_price)

print(f"VALOR A PAGAR: R$ {total1 + total2:.2f}")
