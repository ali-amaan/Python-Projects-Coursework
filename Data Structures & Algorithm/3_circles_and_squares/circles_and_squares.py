# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
#​‌​‌‌​​​‌​‌​​​‌ Implement the count_circles_and_squares function here below

import math


def count_circles_and_squares(length, circles, squares):
    #​‌​‌‌​​​‌​‌​​​‌ Write your code here

    if length < math.sqrt(2):
        if length < 1:
            return 0, 0
        else:
            return 1, 0
    l_rec = length / math.sqrt(2)
    circles, squares = count_circles_and_squares(l_rec, circles, squares)
    return circles + 1, squares + 1


#​‌​‌‌​​​‌​‌​​​‌ A simple example
def main():
    length = 1.1
    circles, squares = count_circles_and_squares(length, 0, 0)
    print("Circles:", circles, "Squares:", squares)


if __name__ == "__main__":
    main()

