def show_magicans(names):
    for i in names:
        print(i)
    # print(name for name in names)


def make_great(names):
    names2 = names[:]
    length = len(names2)
    for i in range(length):
        names2[i] = 'The Great ' + names2[i]
    return names2


names1 = ['1', '2', '3', '4', '5']
make_great = make_great(names1)
show_magicans(names1)
show_magicans(make_great)
