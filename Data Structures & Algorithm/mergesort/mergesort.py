# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
def shift_selection_to_right(a, beg, end):
    for i in range(end, beg, -1):
        a[i] = a[i - 1]


def merge_sort_in_place(a, beg, end):
    if len(a) > 1:
        x = len(a) // 2
        # Sort the two halves
        merge_sort_in_place(a, beg, x)
        merge_sort_in_place(a, x, end)
        b = c = d = 0
        c = x
        len1 = x-beg
        len2 = end-x
        while b < len1 and c < len2:
            if a[b] < a[c]:
                a[d] = a[b]
                b += 1
            else:
                a[d] = a[c]
                c += 1
            d += 1
        while b < len1:
            a[d] = a[b]
            b += 1
            d += 1
        while c < len2:
            a[d] = a[c]
            c += 1
            d += 1
    return a

"""def merge_sort_in_place(arr, l, r):
    # ​‌​‌‌​​​‌​‌​​​‌ Implement this function without creating any new data structures
    if r - l > 1:
        count
        merge_sort_in_place(arr, int((l + r) / 2), r)
        merge_sort_in_place(arr, l, int((l + r) / 2) - 1)"""


def check(input, expected):
    print('Sorting: ' + str(input))
    merge_sort_in_place(input, 0, len(input))
    print('Result: ' + str(input) + '\n')
    return input == expected


if (
        check([4, 7, 4, 1], [1, 4, 4, 7])
        and check([1, 2, 3, 9, 8], [1, 2, 3, 8, 9])
        and check([1], [1])
):
    print('Tests pass! Next, submit your code to A+')
else:
    print('A test failed. Fix your program.')
