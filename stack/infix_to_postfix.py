#!/user/bin/python
# -*-coding:UTF-8-*-

"""将中缀表达式转换为后缀表达式"""
from stack import Stack


def infix_to_postfix(exp: str) -> str:
    st = Stack()
    operators = "+-*/()"
    priority = {"*": 5, "/": 5, "+": 3, "-": 3, "(": 1}
    postfix_lst = []

    for item in exp.split():
        if item not in operators:
            postfix_lst.append(item)
        elif item == "(" or st.is_empty():
            st.push(item)
        elif item == ")":
            while st.top() != "(" and not st.is_empty():
                postfix_lst.append(st.pop())
            if st.top() != "(":
                raise ValueError("Extra operand: ')'")
            st.pop()
        else:
            while not st.is_empty():
                if priority[st.top()] >= priority[item]:
                    postfix_lst.append(st.pop())
                else:
                    break
            st.push(item)

    while not st.is_empty():
        if st.top() == "(":
            raise ValueError("Extra operand: '('")
        postfix_lst.append(st.pop())

    return " ".join(postfix_lst)


if __name__ == '__main__':
    infix_exp = "( 1 + 3 ) * 5 - 8 / 6"
    print(infix_to_postfix(infix_exp))  # 1 3 + 5 * 8 6 / -
