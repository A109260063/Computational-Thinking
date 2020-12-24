## 圖案2:畫出幾何彩虹圖案,畫出房子
import time
import turtle
turtle.bgcolor("blue") #把背景變藍
shelly = turtle.Turtle()
# (1)畫出房子的第一個大正方形
shelly.begin_fill() # 開始填入顏色
shelly.color("gray")
for i in range(4): # 重複4次來畫尺寸為100正方形
    shelly.forward(100)
    shelly.left(90)
shelly.end_fill() # 停止填入顏色
shelly.penup()
shelly.goto(-20,100) #將海龜一到下一個三角形的起點
shelly.pendown()
time.sleep(3)
# (2) 畫出房子的屋頂,一個大三角形
shelly.begin_fill()
shelly.color("red")
shelly.left(60)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.end_fill()
time.sleep(3)
# (3)畫出窗戶
shelly.penup()
shelly.goto(25,80)
shelly.pendown()
shelly.begin_fill()
shelly.color("yellow")
for j in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill()
time.sleep(3)
# (4)隱藏海龜
shelly.hideturtle()