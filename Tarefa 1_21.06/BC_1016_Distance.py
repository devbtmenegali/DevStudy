#ATIVIDADE 1016 Distance

distance = int(input())
relative_speed = 90 - 60                    
time_hours = distance / relative_speed      #Calculo do tempo em horas

time_minutes = time_hours * 60              # Converter o tempo para minutos


print(int(time_minutes), "minutos") 