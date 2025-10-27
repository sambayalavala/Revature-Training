def calculate(m1,m2,m3):
    total = m1+m2+m3
    avg = total/3
    return total,avg
name=input("Enter your name:")
m1=int(input("Enter your first number:"))
m2=int(input("Enter your second number:"))
m3=int(input("Enter your third number:"))
total,avg=calculate(m1,m2,m3)
value:{name}
print(f"total:{total} Avg: {avg}")