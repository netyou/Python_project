class Restaurant:
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


class IceCreamStand(Restaurant):
    def __init__(self,):
        self.ice = ['a', 'b', 'c', 'd']
        for i in self.ice:
            print(i)


icecream = IceCreamStand()
