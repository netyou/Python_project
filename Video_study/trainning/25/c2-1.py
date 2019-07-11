class DictClass:
    """定义一个字典类"""

    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        """删除指定key"""
        if key in self.dict.keys():
            self.dict.pop(key)
            return "del success"
        else:
            print("NOT FOUND")

    def list_get_keys(self):
        """输出key值"""
        return self.dict.keys()

    def update_dic(self, dic2):
        """合并字典"""
        self.dict = dict(self.dict, **dic2)
        return self.dict.values()


dic = DictClass({'one': 1, 'two': 2, 'three': 3})
print(dic.del_dict('one'))
print(dic.list_get_keys())
print(dic.update_dic({'a': 1}))