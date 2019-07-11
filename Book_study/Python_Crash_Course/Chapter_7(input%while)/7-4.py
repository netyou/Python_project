pizzas = "\nPlease input the one you wanna join in: "
pizzas += "\n"+"(If it's over please input 'quit'.)\n"
active = True
while active:
    A = input(pizzas)
    if A == 'quit':
        active = False
        print("Please wait a momnet")
    else:
        print("We will put this " + A + " in your pizza.")