from random import randint


class Die:
    """
    骰子
    """
    def __init__(self):
        self.sides = 6

    def roll_die(self, number):
        self.sides = randint(1, number)
        x = randint(1, self.sides)
        print("A number among side_number: ")
        print(x)


die = Die()
side_number = input("Side number: ")
side_number = int(side_number)
# die.sides = side_number
for i in range(11):
    die.roll_die(side_number)
