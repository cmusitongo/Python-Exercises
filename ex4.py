#The 'cars' variable is equal to 100
#NO NEED FOR SEMI COLONS IN PYTHON
cars = 100
#'_' are underscore characters
space_in_a_car = 4.0
drivers = 30
passengers = 90
#The 'cars_not_driven' variable will equal to cars minus drivers (100 - 30)
cars_not_driven = cars - drivers
#cars_driven is equal to drivers (30)
cars_driven = drivers
#carpool_capacity equals to the cars driven (30) multiplied by space in car (40)
carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car is equal to passengers (90) divided by cars driven (30)
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
