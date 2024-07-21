# Verificação de palíndromo

def verificar_palindromo(texto):
    texto = ''.join(filter(str.isalnum, texto)).lower()  
                             
    if texto == texto[::-1]: 
            print("O texto é um palíndromo!")
    else:
            print("O texto não é um palíndromo")

texto = verificar_palindromo("ovo")


'''
filter(str.isalnum, texto):

str.isalnum: verifica se um caractere é alfanumérico (letra ou número). Retorna True se alfanumérico e False caso contrário.
filter(função, iterável): A função filter recebe uma função (str.isalnum neste caso) e um iterável (o texto) como argumentos. Ela aplica a função a cada elemento do iterável e retorna um novo iterável contendo apenas os elementos para os quais a função retornou True.

''.join(...):

''.join(iterável):  concatenar (juntar) os elementos de um iterável em uma única string. O separador usado entre os elementos é a string vazia (''), o que significa que os caracteres serão unidos.

.lower():

str.lower(): Este método converte todos os caracteres da string para minúsculas.

texto[::-1]:

Essa expressão utiliza a técnica de "slicing" em Python para criar uma cópia invertida do texto original.
Slicing --> texto[inicio:fim:passo].
O passo -1: percorrer a string de trás para frente.
'''
