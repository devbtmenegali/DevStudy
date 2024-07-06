salary = float(input())

if salary <= 400:
    new_salary = salary + (salary*0.15)
    money_earned = salary * 0.15
    means = 0.15 * 100

elif salary > 400 and salary <= 800:
    new_salary = salary + (salary*0.12)
    money_earned = salary * 0.12
    means = 0.12 * 100

elif salary > 800 and salary <= 1200:
    new_salary = salary + (salary*0.10)
    money_earned = salary * 0.10
    means = 0.10 * 100

elif salary > 1200 and salary <= 2000:
    new_salary = salary + (salary*0.07)
    money_earned = salary * 0.07
    means = 0.07 * 100

elif salary > 2000:
    new_salary = salary + (salary*0.04)
    money_earned = salary * 0.04
    means = 0.04 * 100
    
print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {money_earned:.2f}")
print(f"Em percentual: {means:.0f} %")