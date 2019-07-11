def make_album(name, song, number=''):
    album = {
        'name': name,
        'song': song,
    }
    if number:
        album['number'] = number
    return album


while True:
    print("If you wanna quit, input 'quit' anytime.")
    name = input("Please input the name of album: ")
    if name == 'quit':
        break
    song = input("Please input the song in album: ")
    if song == 'quit':
        break
    number = input("Please input the number of the song in this album if you kown: ")
    if number == 'quit':
        break
    album = make_album(name, song, number)
    for k,v in album.items():
        print(k,v)