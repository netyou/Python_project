class School:
    """school"""

    def __init__(self, school_name):
        self.school_name = school_name
        self.student = []
        self.teacher = []


class Grade(School):
    """Grade"""

    def __init__(self, school_name, course, course_t):
        super(Grade, self).__init__(school_name)
        self.course = course
        self.course_t = course_t

    def gradeinfo(self):
        print("This {} in {} has {}".format(self.course, self.school_name, self.course_t))


class SchoolMember(School):
    """member"""

    def __init__(self, school_name, name, age, sex, role):
        super(SchoolMember, self).__init__(school_name)
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role


class Student(SchoolMember):
    def __init__(self, school_name, name, age, sex, role):
        super(Student, self).__init__(school_name, name, age, sex, role)
        if self.role == 'student':
            self.student.append(self.name)
            print(self.student)
        elif self.role == 'teacher':
            self.teacher.append(self.name)
            print(self.teacher)

    def welcome_student(self):
        print("Your name is " + self.name + " age " + str(self.age) + " sex "
              + self.sex + " and your role is a " + self.role + " in " + self.school_name
              + '.\n')


student = Student('BJ', 'a', 17, 'man', 'student')
student2 = Student('BJ', 'b', 17, 'man', 'student')

student.welcome_student()
# schoolmember = SchoolMember
