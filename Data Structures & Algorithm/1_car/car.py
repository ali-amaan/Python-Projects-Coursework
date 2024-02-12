# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
# ​‌​‌‌​​​‌​‌​​​‌ Class to describe a car object
# ​‌​‌‌​​​‌​‌​​​‌ A car has the following attributes: max_tank, tank, consumption, mileage and id

class Car:

    def __init__(self, consumption, name="unregistered vehicle"):
        self.max_tank = 40
        self.tank = self.max_tank  # tank is full when delivered from factory
        self.consumption = consumption
        self.mileage = 0.0
        self.id = name

    # ​‌​‌‌​​​‌​‌​​​‌ Return mileage
    def get_mileage(self):
        return self.mileage

    # ​‌​‌‌​​​‌​‌​​​‌ Return consumption
    def get_consumption(self):
        return self.consumption

    # ​‌​‌‌​​​‌​‌​​​‌ Return tank
    def get_tank_level(self):
        return self.tank

    # ​‌​‌‌​​​‌​‌​​​‌ Drive the wanted distance
    def drive(self, distance):
        max_distance = self.tank / self.consumption * 100
        if max_distance < distance:
            self.mileage += max_distance
            self.tank = 0
            return max_distance
        else:
            self.mileage += distance
            self.tank -= distance * self.consumption / 100
            return distance

    # ​‌​‌‌​​​‌​‌​​​‌ Refuels the car
    def refuel(self, amount):
        self.tank += min(amount, self.max_tank - self.tank)
        return self.tank


# ​‌​‌‌​​​‌​‌​​​‌ Class to describe a car track
# ​‌​‌‌​​​‌​‌​​​‌ A car track has the following attributes: name, distance, cars and nof_cars
# ​‌​‌‌​​​‌​‌​​​‌ Fill in the missing methods

class CarTrack:

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance  # distance of the car track
        self.cars = []  # cars driving on the track (Car-objects)
        self.nof_cars = 0

    # ​‌​‌‌​​​‌​‌​​​‌ Returns the distance of the car track
    def get_distance(self):
        return self.distance

    # ​‌​‌‌​​​‌​‌​​​‌ Returns the list containing the cars in the car track
    def get_cars(self):
        return self.cars

    # ​‌​‌‌​​​‌​‌​​​‌ Returns the number of cars in the car track
    def get_nof_cars(self):
        return self.nof_cars

    def add_car(self, car):
        """ Add a car to the car track and return the number of cars in the track """
        self.nof_cars += 1
        self.cars.append(car)
        return self.nof_cars

    def count_avg_consumption(self):
        """ Count and return the average consumption of the race cars """
        total_consumption = 0.0
        for i in range(self.nof_cars):
            total_consumption += self.cars[i].get_consumption()
        avg_consumption = total_consumption / self.nof_cars
        return avg_consumption

    def get_winner(self):
        """ Return the car with the biggest mileage """
        """ Use of built-in functions such as max() is prohibited """
        winner = self.cars[0]
        for i in range(self.nof_cars):
            if self.cars[i].get_mileage() > winner.get_mileage():
                winner = self.cars[i]
        return winner

    def count_rounds(self, car):
        """ Count how many rounds a car drove, round down to the nearest integer """
        rounds = int(car.get_mileage() / self.distance)
        return rounds

def main():
    carTrackObj = CarTrack("Monaco", 30)
    car1 = Car(10.6, "ZZZ-123")
    car2 = Car(8.1, "ABC-245")
    car3 = Car(13.8, "FOO-634")
    car4 = Car(14.2, "JKL-375")

    carTrackObj.add_car(car1)
    carTrackObj.add_car(car2)
    carTrackObj.add_car(car3)
    carTrackObj.add_car(car4)

    car1.drive(479)
    car2.drive(472)
    car3.drive(531)
    car4.drive(317)

    print("ZZZ-123 =", car1.get_mileage())
    print("ABC-245 =", car2.get_mileage())
    print("FOO-634 =", car3.get_mileage())
    print("JKL-375 =", car4.get_mileage())

    winner = carTrackObj.get_winner()
    print("Winner =", winner.get_mileage())
    print("Winner's Whole Laps =", carTrackObj.count_rounds(winner))
    print("Mean Consumption = ", carTrackObj.count_avg_consumption())

main()