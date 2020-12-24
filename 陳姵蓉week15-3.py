import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black") 

for n in range(6): 
    colors = ["red", "green","blue", "gold", "purple",
"yellow"]
    shelly.color(colors[n]) # A. 選擇第n個正方形的顏色
    for i in range(4): # B. 畫一個尺寸為25的正方形
        shelly.forward(25)
        shelly.left(90)
    shelly.penup() # C. 畫下一個正方形,前進30步(25+5=30)
    shelly.forward(30)
    shelly.pendown()
# (3) 隱藏海龜
shelly.hideturtle()