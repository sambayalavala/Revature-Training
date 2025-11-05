from Arthcalculations import Arthcalculations

n1=int(input("Enter your first number:"))
n2=int(input("Enter your second number:"))

calc=Arthcalculations(n1,n2)
print(f'add:{calc.add()}')
print(f'sub:{calc.sub()}')
print(f'mul:{calc.mul()}')
try:
    res=f'div:calc.div()'
    print(res)
    res=calc.idiv()
except ZeroDivisionError:
    print('0 in denominator')
else:
    print(res)
finally:
    print('Done!!')
