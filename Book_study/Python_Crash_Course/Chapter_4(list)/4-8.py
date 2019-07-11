numbers = [number**3 for number in range(1,11)]
for i in numbers:
    print(i)
numbers2 = []
for i in range(1,11):
    number = i**2
    numbers2.append(number)
for i in numbers2:
    print(i)
print("The first three items in the list are: " )
numbers3 = numbers2[0:3]
print(numbers3)
print("The last three items in the list are: " )
numbers4 = numbers2[-4:-1]
print(numbers4)