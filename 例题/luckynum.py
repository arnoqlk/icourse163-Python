# 提示输入，生成幸运数字
import random
name = input("请输入姓名：")
print('hello! {}'.format(name))
luckynum = ord(name[0]) % 100
print("你的幸运数字是", random.choice(range(luckynum)))

