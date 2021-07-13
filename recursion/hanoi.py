#!/user/bin/python
# -*-coding:UTF-8-*-

"""使用递归解决汉诺塔问题"""


def solve_hanoi(height: int, from_pole: str, to_pole: str, with_pole: str) -> None:
    if height > 0:
        # 将n-1个盘子从第一个柱子A借助第三个柱子C移动到第二个柱子B（这是一个递归过程，参见hanoi.pdf）
        solve_hanoi(height-1, from_pole, with_pole, to_pole)

        # 将第n个盘子移动到第三个柱子C
        print(f"{from_pole}->{to_pole}")

        # 此时第二个柱子有n-1个盘子，把第二个柱子B当作第一个柱子，将原来的第一个柱子当作中间柱子，问题又重新回到第一个递归。
        solve_hanoi(height-1, with_pole, to_pole, from_pole)


if __name__ == '__main__':
    solve_hanoi(5, 'A', 'C', 'B')

# A->C
# A->B
# C->B
# A->C
# B->A
# B->C
# A->C
# A->B
# C->B
# C->A
# B->A
# C->B
# A->C
# A->B
# C->B
# A->C
# B->A
# B->C
# A->C
# B->A
# C->B
# C->A
# B->A
# B->C
# A->C
# A->B
# C->B
# A->C
# B->A
# B->C
# A->C
