#ATIVIDADE 1017 Fuel Spent

spent_time = int(input())
speed_media = int(input())
car_fuel = 12 #km/l

spent_fuel = (speed_media / car_fuel) * spent_time

print(f"{spent_fuel:.3f}")