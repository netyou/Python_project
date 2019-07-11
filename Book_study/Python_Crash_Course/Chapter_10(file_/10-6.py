while True:
    A = input("Please input the first number: \n")
    B = input("Please input the second number: \n")
    try:
        A = int(A)
        B = int(B)
    except ValueError:
        print("Please input 'NUMBER'")
        continue
    else:
        print("{} plus {} equal {}".format(A, B, A+B))
        break
