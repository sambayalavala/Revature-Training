from oop.StudDetails import StudentDetail

ccode = int(input("College Code: "))
cname = input("College Name: ")
rollno = int(input("Student Roll No: "))
name = input("Student Name: ")
m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))

stud = StudentDetail(ccode, cname, rollno, name, m1, m2, m3)

print("\n----- Student Result -----")
print(f"Roll Number  : {stud.get_rollno()}")
print(f"Student Name : {stud.get_sname()}")
print(f"Total Marks  : {stud.calc_tot()}")
print(f"Average Marks: {stud.calc_avg():.2f}")
