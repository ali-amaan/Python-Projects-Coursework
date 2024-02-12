line = input("Base number:\n")
base = int(line)
line = input("Upper limit for the powers:\n")
upper_limit = int(line)
print("Powers:")
value = base
print(value)
value = value * base
while value <= upper_limit:
    print(value)
    value = value * base
