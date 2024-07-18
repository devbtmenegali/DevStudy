#Maria criou uma lista de tarefas que precisa realizar ao longo do dia. 
#Crie um programa em Python que permita adicionar novas tarefas, marcar tarefas 
#como concluídas (removê-las da lista) e imprimir a lista atualizada de tarefas.

lista_de_tarefas = []

def menu_tarefas():
    while True:
        print("Bem vindo a lista de tarefas! Escolha:")
        print("(A) - Adicionar tarefa.")
        print("(C) - Tarefas concluídas")
        print("(S) - Sair")
        opcao = input("O que desejas?")

        if opcao == "A":
            adicionar_tarefas()
        
        elif opcao == "C":
            concluir_tarefas()
        
        elif opcao == "S":
            print("A agenda foi fechada!")
            break
        else:
            print("Opção inválida, escolha corretamente")


def adicionar_tarefas():

    while True:
        tarefa = input("Adicione uma tarefa ou (S)air:").strip()
        if tarefa == "S":
            break
        lista_de_tarefas.append(tarefa)
        
    print("LISTA DE TAREFAS DO DIA!")
    print(lista_de_tarefas)
    
def concluir_tarefas(): 

    while True:
        if lista_de_tarefas == []:
            print("Você deve acrescentar tarefa!")
            break
        else:
            tarefa_c = input("Qual tarefa foi concluída?")
            lista_de_tarefas.remove(tarefa_c)
        
        print("SUA LISTA ATUALIZADA!")
        print(lista_de_tarefas)
        
menu_tarefas()
