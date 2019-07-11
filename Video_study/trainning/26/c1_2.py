from c1_1 import ListInfo


listinf = [1, 2, 3, 4, 5]
listinfo = ListInfo(listinf)
print(listinfo.add_key(6))
print(listinfo.get_key(8, 33))
print(listinfo.update_list([7, 8, 9]))
print(listinfo.del_key())