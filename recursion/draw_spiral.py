#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用turtle模块递归地绘制螺旋线"""
from turtle import Turtle

my_turtle = Turtle()
my_win = my_turtle.getscreen()


def draw_spiral(line_len: int):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(line_len - 5)


if __name__ == '__main__':
    draw_spiral(100)
    my_win.exitonclick()
