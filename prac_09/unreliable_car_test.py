from unreliable_car import UnreliableCar

# Create a new unreliable car
unreliable_car = UnreliableCar("Dodgy", 100, 50)

# Try to drive the car multiple times and print the results
distances = [10, 20, 30, 40, 50]
for distance in distances:
    distance_driven = unreliable_car.drive(distance)
    print(f"Attempted to drive {distance}km. Actually drove {distance_driven}km. {unreliable_car}")
