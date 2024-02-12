# Implement the function dog_age_in_human_years here
def dog_age_in_human_years(age):
    if age <= 1.0:
        hage = age * 15
    if 1.0 < age <= 2.0:
        hage = 15 + (age - 1.0) * 9
    if 2.0 < age:
        hage = 15 + 9 + (age - 2.0) * 5
    print("Your dog is {:.1f} years old in human years!".format(hage))


# Implement the function cat_age_in_human_years here
def cat_age_in_human_years(age):
    if age <= 1.0:
        hage = age * 15
    if 1.0 < age <= 2.0:
        hage = 15 + (age - 1.0) * 10
    if 2.0 < age:
        hage = 15 + 10 + (age - 2.0) * 4
    print("Your cat is {:.1f} years old in human years!".format(hage))


# Implement the function bunny_age_in_human_years here
def bunny_age_in_human_years(age):
    if age <= 0.5:
        hage = (age/0.5) * 16
    if 0.5 < age <= 1.0:
        hage = 16 + ((age - 0.5)/0.5) * 5
    if 1.0 < age:
        hage = 16 + 5 + (age - 1.0) * 6
    print("Your bunny is {:.1f} years old in human years!".format(hage))


def main():
    print("Welcome to the pet age calculator! I will tell your pet's age in human years.")
    choice = 0
    while not 1 <= choice <= 3:
        print("Choose a pet:\n"
              "1: dog\n"
              "2: cat\n"
              "3: bunny")
        choice = int(input())
    age = float(input("How old is your pet?\n"))
    if choice == 1:
        dog_age_in_human_years(age)
    elif choice == 2:
        cat_age_in_human_years(age)
    else:
        bunny_age_in_human_years(age)

main()