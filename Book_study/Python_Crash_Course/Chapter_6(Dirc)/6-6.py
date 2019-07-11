favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'R',
    'phil': 'python',
}
interested_people = ['A', 'B', 'C', 'jen', 'sarah']
for i in interested_people:
    if i in favorite_language.keys():
        print(i.title() + "thank you for investigating. We already know you like " + favorite_language[i].title())
    else:
        print(i.title() + " we want you join us")