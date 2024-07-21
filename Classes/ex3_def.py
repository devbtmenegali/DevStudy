print ("Bem vindo a calculadora")

x = float(input("Digite um número:"))
y = float(input("Digite um número:"))

def adicao():
    return x + y

def subtracao():
    return x - y

def multiplicacao():
    return x * y

def divisao():
    return x / y

resultado_soma = adicao()
resultado_subtracao = subtracao()
resultado_multiplicacao = multiplicacao()
resultado_divisao = divisao()

print(f"A soma de {x} + {y} é {resultado_soma}")
print(f"A subtração de {x} - {y} é {resultado_subtracao}")
print(f"A multiplição de {x} * {y} é {resultado_multiplicacao}")
print(f"A divisão de {x} / {y} é {resultado_divisao}")


