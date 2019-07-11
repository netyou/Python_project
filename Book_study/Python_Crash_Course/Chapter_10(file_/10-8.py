# try:
#     with open('cats.txt') as cats:
#         cat = cats.read()
#         print(cat)
# except FileNotFoundError:
#     pass
#     # print("cats.txt NOT FOUND")
#
# try:
#     with open('dogs.txt') as dogs:
#         dog = dogs.read()
#         print(dog)
# except FileNotFoundError:
#     pass
#     # print("dogs.txt NOT FOUND")


def filename(filen):
    try:
        with open(filen) as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(filen.upper() + ' is not found')


name = ['dogs.txt', 'cats.txt']
for i in name:
    filename(i)




