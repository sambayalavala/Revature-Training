""" Banking Intrest Calculations"""

from mypackage.intrest_calculations import simple_intrest,compound_intrest

prin =float(input("Principal: "))
ny=float(input("Year:"))
roi=float(input("Rate of intrest:"))
si,amt=simple_intrest(prin=prin,ny=ny,roi=roi)
print(f'SI : {si} Amount : {amt}')

amt=compound_intrest(prin=prin,ny=ny,roi=roi)
print(f'Amount: {amt}')
