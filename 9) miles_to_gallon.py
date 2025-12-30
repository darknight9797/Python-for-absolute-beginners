from random import randint

#generates random integers for gallons and miles
gallons = randint(10,25)
miles = randint(200,400)

#calculates and displays the MPG of the car assuming car manufacturers overestimates
#in their claims
print("The car can travel "+ str(miles//gallons)+ " miles per gallon.")
#displays the number of gallons of fuel the car's fuel tank can hold
print("The car's fuel tank can hold "+ str(gallons)+ " gallons of fuel.")
#displays the number of miles that the car can travel on a full tank.
print("The car can travel a total of "+ str(miles)+ " miles on a full tank of gas.")
