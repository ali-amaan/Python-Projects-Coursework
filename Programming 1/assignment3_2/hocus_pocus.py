num1 = int(input("Enter the first number to be printed.\n"))
while num1 <= 0:
    print("Enter a positive number!")
    num1 = int(input("Enter the first number to be printed.\n"))
num2 = int(input("Enter the last number to be printed.\n"))
while num2 <= num1:
    print("Enter a number that is larger than the first number!")
    num2 = int(input("Enter the last number to be printed.\n"))
num1s = str(num1)
num2s = str(num2)
print("Hocus pocus between ", num1s, " - ", num2s, ":", sep='')
for i in range(num1, num2 + 1):
    num = i
    if num % 3 == 0 and num % 5 == 0:
        print("HOCUS POCUS!")
    elif num % 3 == 0:
        print("hocus")
    elif num % 5 == 0:
        print("pocus")
    else:
        print(i)
