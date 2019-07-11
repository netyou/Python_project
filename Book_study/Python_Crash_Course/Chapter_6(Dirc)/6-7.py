person1 = {
    'first_name' : 'Xu',
    'second_name' : 'Weicheng',
    'age' : '24',
    'city' : 'Beijing',
}
person2 = {
    'first_name' : 'Wu',
    'second_name' : 'Ceicheng',
    'age' : '23',
    'city' : 'Shanghai',
}
person3 = {
    'first_name' : 'Cu',
    'second_name' : 'Zeicheng',
    'age' : '22',
    'city' : 'Nanjing',
}
People = [person1, person2, person3]
for person in People:
    for k, v in person.items():
        print(k + ":" + v)