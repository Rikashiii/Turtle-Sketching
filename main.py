import turtle as t

tim = t.Turtle()
t.listen()


def move_forward():
    tim.forward(20)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def move_backward():
    tim.backward(20)


def clear():
    tim.penup()
    tim.clear()
    tim.setposition(0, 0)
    tim.seth(0)
    tim.pendown()


t.onkeypress(move_forward, "w")
t.onkeypress(move_backward, "s")
t.onkeypress(move_left, "a")
t.onkeypress(move_right, "d")
t.onkeypress(clear, "c")

t.exitonclick()
