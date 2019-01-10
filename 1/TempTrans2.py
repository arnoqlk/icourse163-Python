TempStr = input()

if TempStr[0:1] in ['f', 'F']:
	C = (eval(TempStr[1:]) - 32)/1.8
	print("{:.2f}".format(C))

elif TempStr[0:1] in ['c', 'C']:
	F = eval(TempStr[1:]) * 1.8 + 32
	print("{:.2f}".format(F))

else:
	print("Error!!")