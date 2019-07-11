class Employee:
    def __init__(self, name1, name2, age):
        self.name1 = name1
        self.name2 = name2
        self.age = age

    def give_raise(self, raise2=''):
        if raise2 == '':
            self.age += 500
        else:
            self.age += int(raise2)
        return self.age


em = Employee('xu', 'weicheng', 200)
age = em.give_raise()
print(age)