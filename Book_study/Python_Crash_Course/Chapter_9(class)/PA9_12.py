"""管理员和特权"""


import User9_12


class Admin(User9_12.User):
    """
    管理员
    """
    def __init__(self, first_name, last_name,):
        super().__init__(first_name, last_name,)
        self.privileges2 = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show(self):
        print("Admin have this privileges: \n")
        for i in self.privileges:
            print("- " + i)