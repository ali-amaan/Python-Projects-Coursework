# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955


from stack import Stack


def checkParentheses(input_string):
    """Check if input_string has correctly formatted parentheses.
    If parentheses are correct, return True, else return False."""

    # ​‌​‌‌​​​‌​‌​​​‌ Example behaviour:
    # ​‌​‌‌​​​‌​‌​​​‌ ================= ==============================
    # ​‌​‌‌​​​‌​‌​​​‌ input_string      checkParentheses(input_string)
    # ​‌​‌‌​​​‌​‌​​​‌ ================= ==============================
    # ​‌​‌‌​​​‌​‌​​​‌ ()                True
    # ​‌​‌‌​​​‌​‌​​​‌ (()({}))          True
    # ​‌​‌‌​​​‌​‌​​​‌ {aaa(vv)f[gg]df}  True
    # ​‌​‌‌​​​‌​‌​​​‌ a                 True
    # ​‌​‌‌​​​‌​‌​​​‌ (                 False
    # ​‌​‌‌​​​‌​‌​​​‌ (]                False
    # ​‌​‌‌​​​‌​‌​​​‌ aa(b]b)ee         False
    # ​‌​‌‌​​​‌​‌​​​‌ ({)}              False
    # ​‌​‌‌​​​‌​‌​​​‌ ================= ==============================

    stack = Stack()
    l_paranthesis = ["(", "[", "{"]
    r_paranthesis = [")", "]", "}"]
    # ​‌​‌‌​​​‌​‌​​​‌ YOUR CODE HERE
    for i in input_string:
        if i in l_paranthesis:
            stack.push(i)
        elif i in r_paranthesis:
            rp_pos = r_paranthesis.index(i)
            if stack.is_empty():
                return False
            elif stack.top() == l_paranthesis[rp_pos]:
                stack.pop()
    if stack.is_empty():
        return True
    return False
