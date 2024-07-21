#Crie um programa que converta temperaturas de Celsius para Fahrenheit. O programa deve solicitar uma temperatura 
# em Celsius ao usuário e exibir a correspondente em Fahrenheit.
# Calculo -> (0 °C × 9/5) + 32 = 

def conversor_de_temperatura(C):
    C = (C * 9/5) + 32
    return C

C = float(input("Digite a temperatura em C: "))

resultado = conversor_de_temperatura(C)
print(f"A temperatura em F é:{resultado:.2f}")