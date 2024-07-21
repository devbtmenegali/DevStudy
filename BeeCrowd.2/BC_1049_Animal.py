while True:
    try:
        a = input().lower().strip()
        b = input().lower().strip()
        c = input().lower().strip()

        if a == 'vertebrado':
            if b == 'ave':
                if c == 'carnivoro':
                    print("aguia")
                elif c == 'onivoro':
                    print("pomba")
            elif b == 'mamifero':
                if c == 'onivoro':
                    print("homem")
                elif c == 'herbivoro':
                    print("vaca")
        elif a == 'invertebrado':
            if b == 'inseto':
                if c == 'hematofago':
                    print("pulga")
                elif c == 'herbivoro':
                    print("lagarta")
            elif b == 'anelideo':
                if c == 'hematofago':
                    print("sanguessuga")
                elif c == 'onivoro':
                    print("minhoca")
        else:
            raise ValueError("Classificação inválida")
    
    except EOFError:
        break  # Sai do loop quando chegar ao fim do arquivo
    except ValueError as e:
        print(e)
