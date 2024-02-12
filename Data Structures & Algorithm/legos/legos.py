# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
#​‌​‌‌​​​‌​‌​​​‌ Implement the suitable_pieces function here below

def suitable_pieces(width, pieces):
    """
    Returns a tuple (L1, L2) where L1 and L2 are integers in `pieces` which have a sum equal to `width` such that abs(L1 - L2) is largest possible.
    If no pair in `pieces` have a sum equal to width, returns an empty tuple ().
    """
    """tp = len(pieces)
    width = width * 10000000
    pieces.sort()
    final = (0, 0)
    for i in range(0, tp-1):
        for j in range(i+1, tp):
            total = pieces[i] + pieces[j]
            if total == width:
                final = (pieces[i], pieces[j])
                return final
    if final == (0, 0):
        return ()"""
    maxdif = -100
    n = width * 10000000
    n2 = n // 2
    numbers = pieces
    final = ()
    goodnums = {n - x for x in numbers if x <= n2} & {x for x in numbers if x >= n2}
    pairs = list({(n - x, x) for x in goodnums})
    for v1, v2 in pairs:
        diff = abs(v1-v2)
        if maxdif < diff:
            maxdif = diff
            if v1 <= v2:
                final = (v1, v2)
            else:
                final = (v2, v2)
    return final