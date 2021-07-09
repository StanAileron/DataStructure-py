#!/user/bin/python
# -*-coding:UTF-8-*-


"""计算后缀表达式"""
from stack import Stack


def postfix_exp_evaluator(exp: str):
    operators = "+-*/"
    st = Stack()

    for item in exp.split():
        if item not in operators:
            st.push(item)
            continue
        elif st.length() < 2:
            raise ValueError("Short of operands")
        b = int(st.pop())
        a = int(st.pop())
        if item == "+":
            st.push(a + b)
        elif item == "-":
            st.push(a - b)
        elif item == "*":
            st.push(a * b)
        elif item == "/":
            st.push(a / b)
        else:
            pass
    if st.length() == 1:
        return st.pop()
    raise ValueError("Extra operand")


if __name__ == '__main__':
    postfix_exp = "3 5 6 * + 7 -"
    print(postfix_exp_evaluator(postfix_exp))  # 26
