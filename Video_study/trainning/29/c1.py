import random
import math
from c1_1 import *

"""
输入一个三位数与程序随机数比较大小
1 如果大于程序随机数，则分别输出这个三位数的个位、十位、百位
2 如果等于程序随机数，则提示中奖，记100分
3 如果小于程序随机数，则将120个字符输入到文本文件中
    （规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后8个是数字
"""

# 输入函数
while True:
    num = input("请输入一个三位数：")
    random_number = random.randint(100, 999)
    # 检测输入是否是纯数字
    if num.isdigit() and 100 <= int(num) <= 999:
        if int(num) < random_number:
            comparison_small(num)
            break
        elif int(num) > random_number:
            result = comparison_big(random_number)
            break
    else:
        print('请按规定输入')
