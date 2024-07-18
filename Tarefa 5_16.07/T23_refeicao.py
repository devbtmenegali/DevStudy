#Ana está planejando sua semana de refeições e tem listas separadas para 
#café da manhã, almoço e jantar. Crie um programa em Python que 
#combine essas listas em uma única lista usando o método extend()

comida_do_dia = []

def cafe_da_manha ():
    
    lista_manha = []
    for c in range(1,4):
        cafe = input(f" Itens {c} do Café da Manhã: ")
        lista_manha.append(cafe)
    
    print(f"Café da Manhã: {lista_manha}")

cafe_da_manha()