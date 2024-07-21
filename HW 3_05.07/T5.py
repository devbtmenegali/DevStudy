def contador_par_impar(inicio, fim):
    n_par = 0
    n_impar = 0

    for i in range(inicio, fim + 1):

        if i % 2 == 0:
            n_par += 1
        else:
            n_impar += 1

    return n_par, n_impar

pares, impares = contador_par_impar(inicio,fim)
inicio = 1
fim = 20
print(f"Números pares: {inicio}")
print(f"Números Ímpares: {impares}")