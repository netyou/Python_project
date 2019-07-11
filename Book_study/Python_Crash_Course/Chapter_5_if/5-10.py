current_users = ['lilei', 'Xiaoming', 'Meimei', 'Dingding', 'Huahua']
new_users = ['Lilei', 'Xiaoming', 'Lucy', 'Jiji', 'Guagua']
for i in new_users:
    if i.lower() in current_users:
        print("You need change your ID")
    else:
        print("Congralution! This ID is available")