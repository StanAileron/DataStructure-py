#!/user/bin/python
# -*-coding:UTF-8-*-


"""一、将计算表达式解析成二叉树：
1. 如果当前标记是(，就为当前节点添加一个左子节点，并下沉至该节点。
2. 如果当前标记是数字，则将该节点的值设置成这个数字，并返回至父节点。
3. 如果当前标记是[-, +, *, /]的一种，就将当前节点的值设置成这个运算符，为当前节点添加一个右节点，并下沉至该节点。
4. 如果当前表示是)，则跳转至当前节点的父节点。

二、计算解析好的二叉树
f(exp_tree) = f(exp_tree.left_child) +-*/ f(exp_tree.right_child)
1. 如果当前节点是数字，则直接返回这个数字。
2. 如果当前节点是运算符，则递归调用左子树和右子树，并将得到的结果进行相应的运算。
"""
import operator

from tree import BinaryTree


def parse_expression(exp_str: str) -> BinaryTree:
    operators = ['+', '-', '*', '/']
    st = []
    current_tree = BinaryTree(None)

    for item in exp_str.split():
        if item == '(':
            current_tree.insert_left(None)
            st.append(current_tree)
            current_tree = current_tree.get_left_child()
        elif item == ')':
            if len(st) != 0:
                current_tree = st.pop()
        elif item in operators:
            current_tree.set_root_val(item)
            current_tree.insert_right(None)
            st.append(current_tree)
            current_tree = current_tree.get_right_child()
        else:
            current_tree.set_root_val(item)
            current_tree = st.pop()

    return current_tree


def evaluate(parse_tree: BinaryTree):
    # current_root_val = parse_tree.get_root_val()
    # if current_root_val not in ['+', '-', '*', '/']:
    #     return float(current_root_val)
    #
    # try:
    #     if current_root_val == '+':
    #         return operator.add(evaluate(parse_tree.get_left_child()), evaluate(parse_tree.get_right_child()))
    #     elif current_root_val == '-':
    #         return operator.sub(evaluate(parse_tree.get_left_child()), evaluate(parse_tree.get_right_child()))
    #     elif current_root_val == '*':
    #         return operator.mul(evaluate(parse_tree.get_left_child()), evaluate(parse_tree.get_right_child()))
    #     elif current_root_val == '/':
    #         return operator.truediv(evaluate(parse_tree.get_left_child()), evaluate(parse_tree.get_right_child()))
    #     else:
    #         raise ValueError("operand error")
    # except ZeroDivisionError as e:
    #     print("除数不能为零 ", e)
    # except ValueError as e:
    #     print(e)

    # 使用类似后根序遍历的方式实现
    current_root_val = parse_tree.get_root_val()
    if current_root_val not in ['+', '-', '*', '/']:
        return float(current_root_val)

    left_result = evaluate(parse_tree.get_left_child())
    right_result = evaluate(parse_tree.get_right_child())

    try:
        if current_root_val == '+':
            return operator.add(left_result, right_result)
        elif current_root_val == '-':
            return operator.sub(left_result, right_result)
        elif current_root_val == '*':
            return operator.mul(left_result, right_result)
        elif current_root_val == '/':
            return operator.truediv(left_result, right_result)
        else:
            raise ValueError("operand error")
    except ZeroDivisionError as e:
        print("除数不能为零 ", e)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    exp = "( ( 3.2 + 5.3 ) * ( 9.4 - 5.2 ) )"
    exp_tree = parse_expression(exp)
    print(exp_tree.get_root_val())  # *
    print(exp_tree.get_left_child().get_root_val())  # +
    print(exp_tree.get_right_child().get_root_val())  # -

    print(evaluate(exp_tree))  # 35.7
