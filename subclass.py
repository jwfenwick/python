class Student(object):
    def __init__(self,def_name="John Smith",def_grade=9):
        self.name=def_name
        self.grade=def_grade

    def print_student(self):
        print "student name  = {}",format(self.name)
        print "student grade = {}",format(self.grade)

class TempStudent(Student):
    def __init__(self,def_name="zatty zoo",def_grade=0):
        super(TempStudent,self).__init__(def_name="zzzzz",def_grade=99)
        self.name=def_name
        self.grade=def_grade

    
def main():

    student1=Student(def_name="Adam Apple",def_grade=1)
    student2=Student(def_name="Bobby Boyd",def_grade=2)
    student3=Student()
    student4=Student(def_name="Dom Dooby",def_grade=4)

    student5=TempStudent(def_name="yaya yee",def_grade=88)
    student6=TempStudent()

    print student1

    student1.print_student()
    student2.print_student()
    student3.print_student()
    student4.print_student()
    student5.print_student()
    student6.print_student()


if __name__ == "__main__":
    main()
