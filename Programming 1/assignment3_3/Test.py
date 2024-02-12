price = int(input("How much does the apartment cost?\n"))
salary = int(input("How much is your initial monthly salary?\n"))
incper = int(input("How many percent does your salary increase per year?\n"))
saveper = int(input("And how many percent of your salary will you save?\n"))
savings = int(input("How much savings do you have?\n"))
while price <= 0 or salary <= 0 or savings < 0 or incper > 100 or incper < 0 or saveper > 100 or saveper < 1:
    print("Enter only positive values and percentages between 0 - 100!")
    price = int(input("How much does the apartment cost?\n"))
    salary = float(input("How much is your initial monthly salary?\n"))
    incper = float(input("How many percent does your salary increase per year?\n"))
    saveper = float(input("And how many percent of your salary will you save?\n"))
    savings = int(input("How much savings do you have?\n"))
print()
net = price - savings
print("You need ", net, " euros for the apartment.", sep='')
incper = (incper+100)/100
saveper = saveper/100
years = 0
months = 0
amount = 0.0
while amount < net:
    amount = amount + (salary * saveper)
    months = months + 1
    if months % 12 == 0:
        salary = salary * incper
        years = years + 1
        months = 0
if months == 0:
    print("It will take you exactly ", years, " years to save the money for the apartment.", sep='')
else:
    print("It will take you ", years, " years and ", months, " months to save the money for the apartment.", sep='')
