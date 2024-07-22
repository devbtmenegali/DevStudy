
def game_time():

    h_inicio, min_inicio, h_fim, min_fim = map(int,input().split())

    total_minutos_inicio = h_inicio * 60 + min_inicio
    total_minutos_fim = h_fim * 60 + min_fim

    if total_minutos_fim <= total_minutos_inicio:
        total_minutos_fim += 24 * 60

    duracao_minutos = total_minutos_fim - total_minutos_inicio

    horas = duracao_minutos // 60
    minutos = duracao_minutos % 60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

game_time()