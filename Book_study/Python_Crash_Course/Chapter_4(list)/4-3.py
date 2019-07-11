numbers = [number for number in range(1,21)]
print(numbers)
numbers2 = [number for number in range(1,10000001)]
number_min = min(numbers2)
number_max = max(numbers2)
number_sum = sum(numbers2)
print(number_min,number_max,number_sum)
numbers3 = []
for number in range(1,21,2):
    numbers3.append(number)
for number in numbers3:
    print(number)