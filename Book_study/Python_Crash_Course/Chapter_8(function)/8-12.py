def food_in(*name):
    print("You have ordered this: ")
    for i in name:
        print("- " + i)


food_in('A', 'B', 'C')
