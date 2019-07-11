Course_list=[]


class School:
    """学校"""
    def __init__(self, school_name):
        self.school_name = school_name
        self.student_list = []
        self.teacher_list = []

        global Course_list

    def hire(self, obj):
        self.teacher_list.append(obj)
        print("teacher+")

    def enroll(self, obj):
        self.student_list.append(obj)
        print("student+")


class Grade(School):
    """课程"""
    def __init__(self, school_name, course_name, time):
        super(Grade, self).__init__(school_name)
        self.course_name = course_name
        self.time = time
        self.members = []
        Course_list.append(self.course_name)

        print(self.school_name + self.course_name + self.time)


school = School('BJ')
school.hire('Xiaozhou')
school.enroll('Xiaozhang')
grade = Grade('BJ', 'python', '3')
# print()
