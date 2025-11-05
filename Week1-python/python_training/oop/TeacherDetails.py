from oop.College import College

class TeacherDetails(College):
    def __init__(self, ccode, cname, empid, tname, dept):
        super().__init__(ccode, cname)
        self.empid = empid
        self.tname = tname
        self.dept = dept

    def display(self):
        print(f'College Code: {self.ccode}\tCollege Name: {self.cname}\n'
              f'Employee ID: {self.empid}\tTeacher Name: {self.tname}\n'
              f'Department: {self.dept}')
