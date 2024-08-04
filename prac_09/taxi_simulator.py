from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the list of taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi from the list."""
    display_taxis(taxis)
    taxi_choice = input("Choose taxi: ")
    try:
        taxi_choice = int(taxi_choice)
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice], ""
        else:
            return None, "Invalid taxi choice"
    except ValueError:
        return None, "Invalid input; enter a number"


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = Taxi("Default", 0)
    has_chosen_taxi = False
    bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = ""
    while choice != 'q':
        choice = input(">>> ").lower()
        if choice == 'c':
            current_taxi, message = choose_taxi(taxis)
            has_chosen_taxi = True if current_taxi else False
            if message:
                print(message)
        elif choice == 'd':
            if has_chosen_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                distance_driven = current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            if choice != 'q':
                print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(menu)

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == '__main__':
    main()
