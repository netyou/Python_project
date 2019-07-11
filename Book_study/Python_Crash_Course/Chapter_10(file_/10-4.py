while True:
    name = input("input your name: ")
    if name:
        print("Welcome")
    else:
        print("Please input your name: ")
        continue
    with open('guest_book.txt', 'a') as gb:
        gb.write(name + '\n')