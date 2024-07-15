salary = float(input())

if salary <= 2000.0:
    print("Isento")
    
elif 2000.0 < salary <= 3000.0:
    taxes = (salary - 2000.0) * 0.08  
    
elif 3000.0 < salary <= 4500.0:
    taxes = 1000.0 * 0.08 + (salary - 3000.0) * 0.18 
    
else:  # salary > 4500.0
    taxes = 1000.0 * 0.08 + 1500.0 * 0.18 + (salary - 4500.0) * 0.28 

if salary > 2000.0:
    print(f"R$ {taxes:.2f}")

  