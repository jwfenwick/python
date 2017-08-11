"""
Create class objects
Do some operations on the objects
Use object attributes and Methods
"""

class Student(object):
    """ Student object
          contains attributes:
            name   string
            grade  int
          contains methods:
            __init__
            print_student
    """
    def __init__(self,def_name="John Smith",def_grade=9):
        self.name=def_name
        self.grade=def_grade

    def print_student(self):
        print "student name  = {}",format(self.name)
        print "student grade = {}",format(self.grade)

    
def main():

    student1=Student(def_name="Adam Apple",def_grade=1)
    student2=Student(def_name="Bobby Boyd",def_grade=2)
    student3=Student()
    student4=Student(def_name="Dom Dooby",def_grade=4)

    print student1

    student1.print_student()
    student2.print_student()
    student3.print_student()
    student4.print_student()


if __name__ == "__main__":
    main()
