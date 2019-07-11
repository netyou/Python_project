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


user = User('A', 'B')
while True:
    password = input("input your password: ")
    password = int(password)
    if password != 123456:
        user.increment_login_attempts()
    else:
        user.reset_login_attempts()
        break
