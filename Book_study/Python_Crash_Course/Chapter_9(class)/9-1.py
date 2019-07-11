class Restaurant():
    '''
    餐馆
    '''
    def __init__(self, restaurant_name, cuisine_tpye):
        self.name = restaurant_name
        self.type = cuisine_tpye

    def describe_restaurant(self):
        print("A: " + self.name)
        print("B: " + self.type)

    def open_restaurant(self):
        print("OPEN")


restaurant = Restaurant('mingzi', 'dier')
print(restaurant.name + "!")
print(restaurant.type + "!")
restaurant.describe_restaurant()
restaurant.open_restaurant()
