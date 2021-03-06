# 文本进度条.py
#         执行开始
#  0 %[->..........]
# 10 %[*->.........]
# 20 %[**->........]
# 30 %[***->.......]
# 40 %[****->......]
# 50 %[*****->.....]
# 60 %[******->....]
# 70 %[*******->...]
# 80 %[********->..]
# 90 %[*********->.]
# 100%[**********->]

import time
scale = 10
print("{:^20}".format("执行开始"))
for i in range(11):
    a = '*' * i
    b = '.' * (10 - i)
    c = i * 10
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("{:^20}".format("执行结束"))
