
#ATIVIDADE 1020 Age Days

days = int(input())

year = days // 365 #days
days %= 365
month = days // 30 #days
days %= 30

print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{days} dia(s)")
