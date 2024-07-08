#Remember, if the salary is R$ 3,002.00 for example, the rate of 8% is only over R$ 1,000.00, 
# because the salary from R$ 0.00 to R$ 2,000.00 is tax free. In the follow example, the total 
# rate is 8% over R$ 1000.00 + 18% over R$ 2.00, resulting in R$ 80.36 at all. The answer must 
# be printed with 2 digits after the decimal point.


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

  