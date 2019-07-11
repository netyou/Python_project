places = {}
people_active = True
while people_active:
    name = input("\nWhat's your name?")
    place = input("If you could visit one place in the world, where would you go?\n")
    places[name] = place

    A = input("Is there someone else? (yes/no)")
    if A == 'no':
        people_active = False

for name, place in places.items():
    print(name + " wants to go " + place + ".\n")