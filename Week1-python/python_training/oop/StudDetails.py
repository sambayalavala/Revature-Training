from oop.College import College

class StudentDetail(College):
    def __init__(self, ccode, cname, rollno, sname, m1, m2, m3):
        super().__init__(ccode, cname)
        self.__rollno = rollno
        self.__sname = sname
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    # Getter and Setter for Roll Number
    def get_rollno(self):
        return self.__rollno

    def set_rollno(self, rollno):
        self.__rollno = rollno

    # Getter and Setter for Student Name
    def get_sname(self):
        return self.__sname

    def set_sname(self, sname):
        self.__sname = sname

    def calc_tot(self):
        return self.__m1 + self.__m2 + self.__m3

    def calc_avg(self):
        return self.calc_tot() / 3
