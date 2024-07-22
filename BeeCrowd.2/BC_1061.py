
from datetime import datetime

dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(":"))

dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(":"))

inicio = datetime(datetime.now().year, 4, dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)
fim = datetime(datetime.now().year, 4, dia_fim, hora_fim, minuto_fim, segundo_fim)

duration = fim - inicio

dias = duration.days
horas, remainder = divmod(duration.seconds, 3600)  
minutos, segundos = divmod(remainder, 60)       

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")