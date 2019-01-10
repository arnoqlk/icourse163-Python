# 输入数字，返回字符串
weekStr = "星期一星期二星期三星期四星期五星期六星期天"
# 取number值
# i = 0
# while i < 7:
weekId = eval(input("请输入数字(1-7),按0退出！:"))
if weekId not in [0]:
    pos = (weekId - 1) * 3
    weekStr = weekStr[pos:pos + 3]
    print(weekStr)
else:
    print("你输入的有误！")

