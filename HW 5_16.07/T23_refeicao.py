#Ana está planejando sua semana de refeições e tem listas separadas para 
#café da manhã, almoço e jantar. Crie um programa em Python que 
#combine essas listas em uma única lista usando o método extend()

def cafe_da_manha ():
    
    lista_manha = []
    for c in range(1,4):
        cafe = input(f" Itens {c} do Café da Manhã: ")
        lista_manha.append(cafe)
    
    print(f"Café da Manhã: {lista_manha}")
    return lista_manha

def comida_almoco ():
    
    lista_almoco = []
    for a in range(1,4):
        almoco = input(f" Itens {a} do Almoço: ")
        lista_almoco.append(almoco)
    
    print(f"Lista do Almoco: {lista_almoco}")
    return lista_almoco

def comida_jantar ():
    
    lista_jantar = []
    for j in range(1,4):
        jantar = input(f" Itens {a} da janta: ")
        lista_jantar.append(jantar)
    
    print(f"Lista do jantar: {lista_jantar}")
    return comida_jantar

lista_manha = cafe_da_manha()
lista_almoco = comida_almoco()
lista_jantar = comida_jantar()

lista_manha.extend(lista_almoco)
lista_manha.extend(lista_jantar)
print(lista_manha)