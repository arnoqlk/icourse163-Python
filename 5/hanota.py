# 递归问题，汉诺塔
count = 0
def hanota(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanota(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanota(n-1, mid, dst, src)
hanota(3, 'a', 'c', 'b')
print(count)