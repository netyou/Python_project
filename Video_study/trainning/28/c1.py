class TicketPrice:
    """票价系统"""

    def __init__(self, time, age):
        self.exp = 100
        if time in [1, 2, 3, 4, 5]:
            self.inc = 1.2
        else:
            self.inc = 1
        if age < 8:
            self.discount = 0.5
        else:
            self.discount = 1

    def calculation(self, num):
        return self.exp * self.inc * self.discount * num


child = TicketPrice(6, 6)
adult = TicketPrice(6, 16)
print(adult.calculation(2) + child.calculation(1))
