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

menu_tarefas()

#def adicionar_tarefas():
#def concluir_tarefas(): 