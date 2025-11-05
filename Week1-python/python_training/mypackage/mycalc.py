from intrest_calculations import simple_intrest
from shape_calculations import area_of_circle,area_of_react

prin =float(input("Principal: "))
ny=float(input("Year:"))
roi=float(input("Rate of intrest:"))

print(f'Simple intrest: Amount: {simple_intrest(prin= prin, ny=ny,roi=roi)[0]}'
      f'Amount: {simple_intrest(prin= prin, ny=ny,roi=roi)[1]}')

print(f'Area of circle : {area_of_circle(10)}'
      f'Area of react: {area_of_react(10,5)}')