# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
#​‌​‌‌​​​‌​‌​​​‌ Implement the alpha_order function here below

from stack import Stack

def alpha_order(s):
    """Modifies a stack so that its items are in descending order:
    last on bottom, first on top.

    Parameters:
    s (Stack): a Stack with push() and pop() operations
    """
    if not s.is_empty():
        #​‌​‌‌​​​‌​‌​​​‌ YOUR CODE HERE
        temp = s.pop()
        alpha_order(s)
        sortedInsert(s, temp)


def sortedInsert(s, element):
    if s.is_empty() or element < s.top():
        s.push(element)
        return
    else:
        temp = s.pop()
        sortedInsert(s, element)
        s.push(temp)
