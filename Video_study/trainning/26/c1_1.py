class ListInfo:
    """定义一个列表的操作类"""

    def __init__(self, list_info):
        self.list = list_info

    def add_key(self, info):
        # 添加的key必须是字符串或数字
        if isinstance(info, (str, int)):
            self.list.append(info)
            return self.list
        else:
            return "str or int"

    def get_key(self, num, value):
        if num > len(self.list):
            return "Wrong"
        else:
            self.list[num] = value
            return self.list

    def update_list(self, list_new):
        return self.list.extend(list_new)

    def del_key(self):
        if len(self.list) > 0:
            delkey = self.list.pop(-1)
            return delkey
        else:
            return "NO NUMBER"

