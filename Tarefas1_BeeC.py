# ATIVIDADE 2 BEECROWD

A = int(input("A:"))
B = int(input("B:"))
X = A + B

print(f"x = {X}\n")

# ATIVIDADE 3 BEECROWD

R = float(input("R:"))
n = 3.14159
area = n * (R**2)

print(f"A = {area:.4f}")

# ATIVIDADE 4 BEECROWD

A = int(input("n1:"))
B = int(input("n2:"))
adicao = A + B

print(f"SOMA = {adicao}")

# ATIVIDADE 5 BEECROWD

A = int(input("n1:"))
B = int(input("n2:"))
adicao = A + B

print("PROD = ", adicao)

# ATIVIDADE 6 BEECROWD

A = float(input("n1:"))
B = float(input("n2:"))
average = (A + B)/2

print(f"MEDIA = {average:.5f}")
print("end")

# ATIVIDADE 6 BEECROWD

A = float(input("n1:"))*2
B = float(input("n2:"))*3
C = float(input("n3:"))*5
average = (A+B+C)/10

print(f"MEDIA = {average:.1f}")

# ATIVIDADE 7 BEECROWD

A = int(input())
B = int(input())
C = int(input())
D = int(input())
Difer = (A*B) - (C*D)

print(f"DIFERENCA = {Difer}")

# ATIVIDADE 8 BEECROWD

number = int(input())
N_Hora = int(input())
Valor_Hora = float(input())
Salary = N_Hora * Valor_Hora

print(f"NUMBER = {number}")
print(f"SALARY = U$ {Salary:.2f}")

# ATIVIDADE 9 BEECROWD

name = str(input())
salary = float(input())
sold = float(input())
bonus = salary + (sold*0.15)

print(f"TOTAL = {bonus:.2f}")

# ATIVIDADE 1010 BEECROWD


split() -> Separador: Você pode indicar um caractere ou uma sequência de caracteres que servirá 
como delimitador para dividir a string. Se nenhum separador for fornecido, a função dividirá a 
string em espaços em branco (espaços, tabulações, novas linhas, etc.).

product1_code, product1_units, product1_price = input().split()         
product2_code, product2_units, product2_price = input().split()
total1 = int(product1_units) * float(product1_price)
total2 = int(product2_units) * float(product2_price)

print(f"VALOR A PAGAR: R$ {total1 + total2:.2f}")
print("END")


# ATIVIDADE 1011 BEECROWD

R = float(input())
pi = 3.14159
volume = (4/3)*(pi*R**3)

print(f"VOLUME = {volume:.3f}")


# ATIVIDADE 1012 BEECROWD

#map() -> ferramenta que permite aplicar uma determinada função a cada elemento de um 
#objeto iterável (como uma lista, tupla ou conjunto) e retorna um novo objeto iterador 
#com os resultados.

A, B, C = map(float,input().split())
pi = 3.14159

triangle = (A * C) / 2
circle = (C ** 2) * pi
trapezium = ((A + B) * C) / 2
square = B ** 2
rectangle = A * B

print(f"TRIANGULO = {triangle:.3f}")
print(f"CIRCULO = {circle:.3f}")
print(f"TRAPEZIO = {trapezium:.3f}")
print(f"QUADRADO = {square:.3f}")
print(f"RETANGULO = {rectangle:.3f}")
print("END")


#ATIVIDADE 1013 BEECROWD

a, b , c = map(int,input().split())

maiorAB = (a + b + abs(a-b))/2                  #Esta equação vai descobrir o maior valor entre "a" e "b".
maior = (maiorAB + c + abs(maiorAB - c))/2      #Esta equação vai descobrir o maior valor entre o maiorAB e "c".
                                                #A parte abs(a - b) garante que a diferença entre a e b seja ->
print(f"{maiorAB} é o maior")                       #positiva, independentemente de qual seja o maior. Isso permite que a fórmula funcione corretamente


#ATIVIDADE 1014 BEECROWD

X = int(input())
Y = float(input())

media = X/Y

print(f"{media:.3f} km/l")


#ATIVIDADE 1015 BEECROWD

import math                                     #permite que você utilize as funções e constantes presentes no módulo math (funções matemáticas).

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   #sqrt é raiz quadrada.

print(f"{distance:.4f}")


#ATIVIDADE 1016 BEECROWD

distance = int(input())
relative_speed = 90 - 60                    
time_hours = distance / relative_speed      #Calculo do tempo em horas

time_minutes = time_hours * 60              # Converter o tempo para minutos


print(int(time_minutes), "minutos") 

#ATIVIDADE 1017 BEECROWD

spent_time = int(input())
speed_media = int(input())
car_fuel = 12 #km/l

spent_fuel = (speed_media / car_fuel) * spent_time

print(f"{spent_fuel:.3f}")


#ATIVIDADE 1018 BEECROWD --> não funcionou.

value = int(input())
banknotes = [100, 50, 20, 10, 5, 2, 1]

print(value)

for notes in banknotes:                                      # Itera sobre as notas disponíveis
    quantidade = value // notes                              # Calcula quantas notas deste valor são necessárias,o operador // é chamado de divisão inteira ou floor division. Ele realiza a divisão entre dois números e retorna o quociente inteiro
    
    if quantidade > 0:                                      # Se for necessário pelo menos uma nota, imprime a informação
        print(f"{quantidade} nota(s) de R$ {notes},00")      # Atualiza o valor restante após usar as notas deste valor
    
    value %= notes


#ATIVIDADE 1019 BEECROWD

seconds = int(input())

hours = seconds // 3600     
seconds %= 3600           
minutes = seconds // 60   
seconds %= 60                                  # %= é usado para atualizar o valor de uma variável calculando o resto da divisão da variável pelo valor à direita do operador e, em seguida, atribuindo esse resto de volta à variável.

print(f"{hours}:{minutes:02d}:{seconds:02d}")  #:02d garante que minutos e segundos sejam exibidos com dois dígitos, adicionando um zero à esquerda


#ATIVIDADE 1020 BEECROWD

days = int(input())

year = days // 365 #days
days %= 365
month = days // 30 #days
days %= 30

print(f"{year} anos")
print(f"{month} meses")
print(f"{days} dias")


#ATIVIDADE 1021 - Banknotes and Coins



#ATIVIDADE 1035 -> Selection Test 1

A, B, C, D = map(int, input().split())

if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


# 1036 -> Bhaskara's Formula

# 1037 ->Interval