celsius = int(input("Enter temperature in Celsius: "))

def fahrenheit(celsius):
    return(celsius*1.8) + 32
    
print("The Fahrenheit equivalent of "+str(celsius)+" degrees Celsius is "+str(fahrenheit(celsius)))
