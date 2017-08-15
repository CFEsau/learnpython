cars = 100                       # number of cars
space_in_a_car = 4               # number of passenger seats in each car
drivers = 30                     # number of drivers
passengers = 90                  # number of passengers
cars_not_driven = cars - drivers # number of cars not in use
cars_driven = float(drivers)     # number of cars in use
# carpool capacity, number of people that can be carpooled when all cars in use
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers per car for a given number of passengers
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
