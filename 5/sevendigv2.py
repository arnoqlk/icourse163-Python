# 绘制七段数码管
import turtle, time
# 间隔
def drawGap():
    turtle.penup()
    turtle.fd(5)
# 划线
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else \
    turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
# 绘制连段数字
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else\
    drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else\
    drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else\
    drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else\
    drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else\
    drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else\
    drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else\
    drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
# 获取date格式,%y-%m=%d+
def drawDate(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 28, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 28, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=('Arial', 28, 'normal'))
        else:
            drawDigit(eval(i))
# 主函数
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
    
