# Crie um programa que solicite ao usuário uma senha. O programa deve continuar pedindo a senha até que 
# o usuário digite a senha correta, que é "senha123".

def verificador_de_senha(senha):
    password = input("Digite a Senha: ")

    while True:
        if password == senha:
            print("Você acessou!")
            break
        else:
            print("Tente novamente")
            password = input("Digite a Senha: ")

verificador_de_senha("Senha123")