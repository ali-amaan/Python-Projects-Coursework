import math


def calculate_cost(consumption, distance, gas_price, rent, time):
    cost = (rent * math.ceil(time)) + ((consumption/100) * distance * gas_price)
    return cost


def main():
    gas_price = float(input("How much does gas cost (per litre)?\n"))
    brent = float(input("Enter the hourly rent for the big van:\n"))
    btime = float(input("Enter the estimated rental time (hours) for the big van:\n"))
    bdistance = float(input("Enter estimated driving distance (km) for the big van:\n"))
    bconsumption = float(input("Enter fuel consumption (litres / 100 km) for the big van:\n"))
    srent = float(input("Enter the hourly rent for the small van:\n"))
    stime = float(input("Enter the estimated rental time (hours) for the small van:\n"))
    sdistance = float(input("Enter estimated driving distance (km) for the small van:\n"))
    sconsumption = float(input("Enter fuel consumption (litres / 100 km) for the small van:\n"))
    bcost = calculate_cost(bconsumption, bdistance, gas_price, brent, btime)
    scost = calculate_cost(sconsumption, sdistance, gas_price, srent, stime)
    bcost_rounded = round(bcost, 2)
    scost_rounded = round(scost, 2)
    print("Renting the bigger van would cost {:.2f} euros and renting the smaller van would cost {:.2f} euros.".format(bcost_rounded, scost_rounded))
    if bcost == scost or bcost < scost:
        print("You should rent the big van.")
    elif bcost > scost:
        print("You should rent the small van.")

main()
