idade = int(input ("Qual a sua idade?"))
valor = 20
resultado = 0

if idade <= 12:
    resultado = valor / 2
    print (f"sua entrada custará, {resultado}")

elif idade > 12 and idade < 18:
    resultado =  valor / 2 + 5
    print (f"sua entrada custará {resultado}")

else:
    print (f"sua entrada custará {valor}")

