# 绘制七彩圆圈
import turtle
color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
for i in range(7):
    c = color[i]
    turtle.color('white', c)
    turtle.begin_fill()
    turtle.right(360/7)
    turtle.circle(50)
    turtle.end_fill()

turtle.done()
