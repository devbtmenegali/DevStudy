#Potência: Faça um programa que solicita uma base e um expoente, e calcula a potência 
#da base elevada ao expoente e exibe o resultado.

base, expoente = map(float,input().split())

resultado = base ** expoente

print(f"O resultado é: {resultado:.1f}")