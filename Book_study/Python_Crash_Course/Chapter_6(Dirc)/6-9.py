favorite_places = {
    'xiaozhang': {
        'first': 'Changcheng',
        'second': 'gudong',
        'third': 'xinxilan',
    },
    'xiaoming': {
        'first': 'dada',
        'second': 'dd',
    }
}
for name,place in favorite_places.items():
    print(name + " likes: ")
    for k,v in place.items():
        print(k + ":" + v)
    print("\n")