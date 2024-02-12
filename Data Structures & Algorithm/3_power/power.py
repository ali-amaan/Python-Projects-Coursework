# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955

# ​‌​‌‌​​​‌​‌​​​‌ Implement the power function here below
# ​‌​‌‌​​​‌​‌​​​‌ You can expect to base and exponent to be 0 or greater.
# ​‌​‌‌​​​‌​‌​​​‌ Both of the paramaters are not allowed to be 0 at the same time

def power(base, exponent):
    # ​‌​‌‌​​​‌​‌​​​‌Write your code here
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base*power(base, exponent - 1)


def main():
    # ​‌​‌‌​​​‌​‌​​​‌Try your function
    base = 5
    exponent = 3
    print("{} ^ {} = {}".format(base, exponent, power(base, exponent)))


if __name__ == "__main__":
    main()
