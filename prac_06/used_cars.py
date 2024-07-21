"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    car_name = input("Enter your car name: ")
    car = Car(100)
    car.name = car_name
    car.add_fuel(20)
    car.drive(115)
    print(car)


main()
