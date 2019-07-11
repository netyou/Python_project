class User:
    '''
    用户信息
    '''

    def __init__(self, first_name, last_name, *info):
        self.fname = first_name
        self.lname = last_name
