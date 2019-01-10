# 循环提示用户输入小爱好
hob = ''
for i in range(3):
    s = input("请输入最多三个小爱好，按q或Q退出：")
    if s in ['q', 'Q']:
        break
    hob += s + ','
print(hob)

