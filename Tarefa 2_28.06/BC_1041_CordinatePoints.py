x,y = map(float,input().split())

if x > 0 and y > 0:
    print (f"Q1")

if x > 0 and y < 0:
    print (f"Q4")

if x < 0 and y < 0:
    print (f"Q3")

if x < 0 and y > 0:
    print (f"Q2")

if x == 0 and y == 0:
    print (f"Origem")