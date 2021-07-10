#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用turtle绘制分形树"""
from turtle import Turtle

my_turtle = Turtle()
my_win = my_turtle.getscreen()


def draw_tree(branch_len: int):
    if branch_len > 5:
        my_turtle.forward(branch_len)

        my_turtle.right(20)
        draw_tree(branch_len - 15)

        my_turtle.left(40)
        draw_tree(branch_len - 10)

        my_turtle.right(20)  # 退回到上一个节点
        my_turtle.backward(branch_len)


if __name__ == '__main__':
    draw_tree(100)
    my_win.exitonclick()
