#declaring the number of cars available
cars = 100
#declaring the space available in the cars
space_in_a_car = 4.0
#initializing the value for drivers
drivers = 30
#initializing the value of the passengers
passengers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capcity = cars_driven * space_in_a_car
avg_passenger_per_car = passengers / cars_driven

print("There are", cars ,"cars available")
print("There are only", drivers , "drivers available")
print("There will be", car_not_driven , "empty cars today")
print("We can transport", carpool_capcity , "people today")
print("We have", passengers , "to carpool today.")
print("We need to put about", avg_passenger_per_car ,"in each car")
