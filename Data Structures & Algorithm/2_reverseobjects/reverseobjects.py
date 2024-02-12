# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
# ​‌​‌‌​​​‌​‌​​​‌ Implement the reverseObjects function here below

from stack import Stack


def reverseObjects(sequence):
    """Returns the contents of sequence reversed in a list."""
    reversed_list = []
    if sequence is None:
        return reversed_list
    stack = Stack()
    counter = 0
    for i in sequence:
        stack.push(i)
        counter += 1

    for x in range(counter):
        reversed_list.append(stack.pop())

    # ​‌​‌‌​​​‌​‌​​​‌ Do something with stack and sequence
    # ​‌​‌‌​​​‌​‌​​​‌ ...
    # ​‌​‌‌​​​‌​‌​​​‌ ...
    # ​‌​‌‌​​​‌​‌​​​‌ ...
    # ​‌​‌‌​​​‌​‌​​​‌ Return the sequence reversed

    return reversed_list
