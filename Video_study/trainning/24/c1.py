import random
import math


# 输入函数
num = input("请输入一个三位数：\n")
# 检测输入是否是纯数字
if num.isdigit():
    # 输入函数输入的是字符类型
    if 100 <= int(num) <= 999:
        # 判断输入的数，与系统随机数比较大小
        pass

else:
    print("wrong")