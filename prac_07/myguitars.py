import csv
from guitar import Guitar


def read_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)


def add_guitar(guitars):
    """Add a new guitar to the list from user input."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: "))
    guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = 'guitars.csv'
    guitars = read_guitars(filename)

    guitars.sort()
    print("\nSorted Guitars (by year):")
    display_guitars(guitars)

    add_guitar(guitars)

    save_guitars(filename, guitars)
    print("\nGuitars after adding new ones:")
    display_guitars(guitars)


if __name__ == "__main__":
    main()

