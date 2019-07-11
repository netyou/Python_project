name = input("inpur your name: ")
with open('guest.txt','w') as name_write:
    name_write.write(name)