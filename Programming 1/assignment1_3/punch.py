line = input("Enter the amount of the alcoholic drink (l).\n")
Alcoholic_Drink = float(line)
line = input("Enter the alcohol content of the alcoholic drink (%).\n")
Alcohol_Content = float(line)
line = input("How much non-alcoholic drink do you want to add (l)?\n")
Non_Alcoholic_Drink = float(line)
Drink_Strength = 100 * (((Alcohol_Content / 100) * Alcoholic_Drink) / (Alcoholic_Drink + Non_Alcoholic_Drink))
print("Alcohol content of the drink is ", Drink_Strength, " %.")
