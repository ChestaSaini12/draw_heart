# draw heart using turtle
import turtle
wn = turtle.Screen()
wn.bgcolor("sky blue")
heart = turtle.Turtle() # "heart" is turtle name 
heart.up()
heart.goto(0,-100)
heart.down()
heart.begin_fill()
heart.fillcolor('red') # filling process begins
# start drawing the heart shape
heart.left(140)
heart.forward(180)
heart.circle(-90,200)
# draw the left side
heart.setheading(60)
heart.circle(-90, 200)
# finid drawing 
heart.forward(180)
heart.end_fill()
heart.hideturtle()
wn.mainloop()
