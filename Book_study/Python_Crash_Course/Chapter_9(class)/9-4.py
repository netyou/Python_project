class Restaurant():
    '''
    餐馆
    '''
    def __init__(self, restaurant_name, cuisine_tpye):
        self.name = restaurant_name
        self.type = cuisine_tpye
        self.number_serverd = 0

    def describe_restaurant(self):
        print("A: " + self.name)
        print("B: " + self.type)

    def open_restaurant(self):
        print("OPEN")

    def set_number_served(self, number):
        self.number_serverd = number

    def increment_number_served(self, number):
        self.number_serverd += number


restaurant = Restaurant('mingzi', 'dier')
print(restaurant.name + "!")
print(restaurant.type + "!")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(str(restaurant.number_serverd) + "!")
restaurant.set_number_served(20)
print(str(restaurant.number_serverd) + "!")
restaurant.increment_number_served(5)
print(str(restaurant.number_serverd) + "!")

