
hora_inicial, hora_final = map(int,input().split())

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
    print(f"O JOGO DUROU {duracao} HORA(S)")

else:
    hora_inicial > hora_final
    duracao2 = 24 - hora_inicial + hora_final
    print(f"O JOGO DUROU {duracao2} HORA(S)")