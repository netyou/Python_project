class Admin:
    """管理员"""

    def __init__(self):
        self.linux = 'Linux'
        self.python = 'python'
        self.teacher = 'XiaoZhou'
        self.student = 'XiaoZhang'


class BeiJing(Admin):
    """北京校区"""

    def __init__(self):
        super(BeiJing, self).__init__()
        self.course = self.linux + '1time'

    def teacher_in_beijing(self):
        self.teacher_beijing = self.teacher
        return 'Day02'

    def student_in_beijing(self):
        self.student_beijing = self.student






class ChengDu(Admin):
    """成都校区"""

    def __init__(self):
        super(Admin, self).__init__()
        self.course = self.python + '3time'





