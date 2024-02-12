# Implement the function calculate_and_print here.
def calculate_and_print(shape, base, height):
    if shape == 't':
        area = 0.5*base*height
        print("The area is ", area, " square meters.", sep='')
    else:
        area = base*height
        print("The area is ", area, " square meters.", sep='')


def main():
    print("Choose a shape:")
    print("r - rectangle")
    print("t - triangle")
    shape = input()
    base = float(input("Enter the length of the base (m):\n"))
    height = float(input("Enter the height (m):\n"))
    calculate_and_print(shape, base, height)


main()
