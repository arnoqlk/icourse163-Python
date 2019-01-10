# body mass index v.01
height, weight = eval(input("请输入身高和体重[逗号分隔]："))
bmi = weight / pow(height, 2)
print("bmi的值为：{:.2f}".format(bmi))

# 判断 18.5 25 30
who = ""
if bmi < 18.5:
    who = "偏瘦"
elif 18.5 <= bmi < 25:
    who = "标准"
elif  25 <= bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"

print("国际标准为：{}".format(who))


