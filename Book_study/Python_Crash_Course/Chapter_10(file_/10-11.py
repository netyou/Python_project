import json


def open_file(file_name, number2):
    try:
        with open(file_name) as ns:
            number = json.load(ns)
        return number
    except FileNotFoundError:
        write_file(file_name, number2)


def write_file(file_name, number3):
    # name = input('your name: \n')
    # number = input('your number: \n')
    with open(file_name, 'a') as ns:
        json.dump(number3 + '\n', ns)
        print("You have join in {}".format(number3))


def show_number(file_name2):
    number = input("your number: ")
    dirc = open_file(file_name2, number)
    # dirc = open_file(file_name)
    if number in dirc:
        print("This is your number: {}".format(number))
    else:
        write_file(file_name, number)


file_name = 'number_store'
while True:
    show_number(file_name)
