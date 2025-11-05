from oop.Employee import Employe


empid=int(input('Emp id: '))
ename = input('E Name: ')
bp = float(input('Basic Pay: '))

employee=Employe(empid,ename,bp)

print(f'Emp id: {employee.empid} \n Name: {employee.ename} \n'
      f'Gross Pay: {employee.calc_grosspay()}\n'
      f'Net Pay: {employee.calc_netpay()}')
