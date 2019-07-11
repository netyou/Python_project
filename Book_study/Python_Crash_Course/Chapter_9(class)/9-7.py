class User:
    '''
    users
    '''

    def __init__(self, first_name, last_name,):
        self.fname = first_name
        self.lname = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.fname + ',' + self.lname)

    def greet_user(self):
        print("Hello! " + self.fname + "," + self.lname)

    def increment_login_attempts(self,):
        self.login_attempts += 1
        print("Wrong: " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
        print("Welcome")


class Admin(User):
    '''
    管理员
    '''

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


admin = Admin('A', 'B')
admin.privileges2.show()
admin.describe_user()
