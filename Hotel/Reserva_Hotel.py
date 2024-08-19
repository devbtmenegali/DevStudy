def verificar_disponibilidade():

    quartos = {101: "Disponível",
               102: "Disponível",
               201: "Disponível",
               202: "Disponível",
               301: "Disponível",
               302: "Disponível"}

    while True:

        disponibilidade = input("Digite o número do quarto para verificar disponibilidade: ")

        if disponibilidade.lower() == 'sair':
            break 
        try:
            numero_quarto = int(disponibilidade)
        except ValueError:
            print("Digite um valor válido para essa operação!")
            continue

        if numero_quarto in quartos:
            status = quartos[numero_quarto]
            print(f"O quarto {numero_quarto} está {status}.")

        if status == "Disponível":
                return numero_quarto 
        
        else:
            print(f"O quarto {numero_quarto} não existe.")
 
    return None

def reservar_quarto(quartos, numero_quarto):

    if numero_quarto is None:  # Verifica se um quarto válido foi encontrado
        return

    alugar_quarto = input("Você deseja ocupar o quarto? S/N: ").upper()

    if alugar_quarto == "S":
        quartos[numero_quarto] = "Ocupado"
        print(f"O quarto {numero_quarto} foi reservado com sucesso!")

    elif alugar_quarto == "N":
        print("Ok, o quarto continua disponível.")
    
    else:
        print("Resposta inválida. Por favor, digite 'S' ou 'N'.")


quarto_disponivel = verificar_disponibilidade()
reservar_quarto(quartos, quarto_disponivel) 
    