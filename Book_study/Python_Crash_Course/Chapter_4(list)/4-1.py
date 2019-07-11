pizza = ['apple', 'bear', 'banana']
for i in pizza:
    print("I like this " + i + ".")
print("I really like pizza")
friend_pizzas = pizza[:]
pizza.append("orange")
friend_pizzas.append("pig")
print("My favorite pizzas are: ")
for i in pizza:
    print(i)
print("My friend's favorite pizzas are: ")
for i in friend_pizzas:
    print(i)