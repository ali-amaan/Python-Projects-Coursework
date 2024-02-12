allowed = 0
not_allowed = 0
num = int(input("How many heights will be entered?\n"))
while num <= 0:
    print("Enter a positive value!")
    num = int(input("How many heights will be entered?\n"))
print("Enter the heights of the children on separate lines.")
for i in range(1, num+1):
    height = int(input())
    if height >= 140:
        allowed = allowed + 1
    else:
        not_allowed = not_allowed + 1
print("There are ", num, "children")
print(allowed, "of the children are allowed and ", not_allowed, " are not allowed on the roller coaster.")
