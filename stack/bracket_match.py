#!/user/bin/python
# -*-coding:UTF-8-*-


"""括号匹配"""
from stack import Stack


def bracket_match(string: str) -> bool:
    s = Stack()
    open_brackets = "([{"
    close_brackets = ")]}"
    opposite = {"(": ")", "[": "]", "{": "}"}

    for item in string:
        if item in open_brackets:
            s.push(item)
        elif item in close_brackets:
            if s.length() < 1:
                return False
            if opposite[s.pop()] != item:
                return False
        else:
            pass
    return True


if __name__ == '__main__':
    right_str = "([{()[(){}]{}}])"
    wrong_str = "{()[({}])]}"
    print(bracket_match(right_str))  # True
    print(bracket_match(wrong_str))  # False
