class Student:
    """定义一个学生的类"""

    # def __init__(self, student_name, student_age, student_grade_enlish,
    #              student_grade_math, student_grade_chinese):
    #     """初始化"""
    #     self.name = student_name
    #     self.age = student_age
    #     self.grade_english = student_grade_enlish
    #     self.grade_math = student_grade_math
    #     self.grade_chinese = student_grade_chinese
    def __init__(self, student_name, student_age, student_scorse):
        self.name = student_name
        self.age = student_age
        self.scorse = student_scorse

    def get_name(self):
        return self.name
        print("name: {}".format(self.name))

    def get_age(self):
        return self.age
        print("age: {}".format(self.age))

    def get_course(self):
        return max(self.scorse)
        print("1")

