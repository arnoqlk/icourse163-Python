# temperature transfer

Temp = input("请输入温度值(F/C):")

# 输入摄氏度

if Temp[-1] in ['C','c']:
	F = 1.8 * eval(Temp[0:-1]) + 32
	print("{:.2f}".format(F))

# 输入华氏度

elif Temp[-1] in ['F','f']:
	C = (eval(Temp[0:-1]) - 32) / 1.8
	print("{:.2f}".format(C))

else:
	print("Error!!")

# TemStr = input("input temp(F/C):")

# if TemStr[-1] in ['F', 'f']:
#    C = (eval(TemStr[0:-1]) - 32)/1.8
#    print("{:.2f}".format(C))
# elif TemStr[-1] in ['C', 'c']:
#    F = 1.8*eval(TemStr[0:-1]) + 32
#    print("{:.2f}".format(F))
# else:
#    print("Error!")
