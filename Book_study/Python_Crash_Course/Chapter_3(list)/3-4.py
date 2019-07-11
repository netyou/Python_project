name_invented = ['xuweicheng', 'zhangbo', 'zhuyifan', 'daipaiyu']
for i in name_invented:
    print("Congralution! You are invented in this party, " + i.title())
print("It's shame that " + name_invented[0].title() + " can't come with us")
del name_invented[0]
name_invented.insert(0,'wangluodan')
print(name_invented)
name_invented.insert(1,'lizhiyao')
name_invented.append('liuhaiyang')
for i in range(5):
    print("invented " + name_invented[i])
num1 = name_invented.pop(0)
print("Sorry, you are not in the list of invented " + num1)
num2 = name_invented.pop(0)
print("Sorry, you are not in the list of invented " + num2)
num3 = name_invented.pop(0)
print("Sorry, you are not in the list of invented " + num3)
num4 = name_invented.pop(0)
print("Sorry, you are not in the list of invented " + num4)
for i in name_invented:
    print("Remember to come on time " + i.title())
del name_invented[0]
del name_invented[0]
print(name_invented)