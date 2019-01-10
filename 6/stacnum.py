# 统计值
def getNum():
    nums = []
    inum = input("请输入数字(回车退出！)")
    while inum != "":
        nums.append(eval(inum))
        inum = input("请输入数字（回车退出！）")
    return nums


# mean
def mean(numbers):
    s = 0.0
    for n in numbers:
        s = s + n
    return s / len(numbers)


# sdav
def sdev(numbers, mean):
    sdev = 0.0
    for n in numbers:
        sdev = sdev + (n - mean)**2
    return pow(sdev / (len(numbers) - 1), 0.5)


# medium
def medium(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


n = getNum()
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}".format(m, sdev(n, m), medium(n)))
