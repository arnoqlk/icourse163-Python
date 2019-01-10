# 星号三角形
a = input("please input a odd: ")
for i in range((eval(a)+1)//2):
    num = '*' * (2*i+1)
    print("{0:^{1}}".format(num, eval(a)))

# n = eval(input())
# for i in range(1,n+1,2):
#     print("{0:^{1}}".format('*'*i, n))