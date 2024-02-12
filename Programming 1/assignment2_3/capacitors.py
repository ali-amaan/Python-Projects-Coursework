i = 1
capacitance = 0.0
line = input("How many capacitors are there?\n")
cap = int(line)
while cap < 1:
    print("Enter a positive value!")
    line = input("How many capacitors are there?\n")
    cap = int(line)
line = input("Are the capacitors connected:\n1. in series\n2. in parallel?\n")
choice = int(line)
while choice != 1 and choice != 2:
    print("Invalid choice!")
    line = input("Are the capacitors connected:\n1. in series\n2. in parallel?\n")
    choice = int(line)
while i <= cap:
    line = input("Enter the capacitance for the next capacitor: ")
    value = float(line)
    if choice == 2:
        capacitance = capacitance + value
    elif choice == 1 and i > 1:
        capacitance = (capacitance * value)/(capacitance + value)
    elif choice == 1 and i == 1:
        capacitance = value
    i = i + 1
print("The total capacitance of the capacitors is ", capacitance, " F.")
