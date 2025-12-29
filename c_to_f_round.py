celsius = int(input("Enter temperature in Celsius: "))

def fahrenheit(celsius):
    #The second argument of the round() is 1 since we only want the Fahrenheit 
    #temperature to be displayed with one number after the decimal point.
    return round((celsius*1.8) + 32,1)
    
print("The Fahrenheit equivalent of "+str(celsius)+" degrees Celsius is "+str(fahrenheit(celsius)))