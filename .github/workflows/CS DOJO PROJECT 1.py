# A discussion between Fahrenheit and his brother Celsius
def Fahrenheit_to_Celsius(fer):
    Celsius=(fer - 32) * 5/9
    return Celsius
fer=float(input("Enter the Fahrenheit Temperature:  "))
89
print("Celsius Temperature:")
print(Fahrenheit_to_Celsius(fer))

#A discussion between Celsius and his brother Fanrenheit
def Celsius_to_Fahrenheit(cel):
    Fahrenheit=(cel * 1.8) + 32
    return Fahrenheit 
cel=float(input("Enter the Celsius Temperature:   "))
print("Fahrenheit Temperature: ")
print(Celsius_to_Fahrenheit(cel))

#A discussion between Inches and her cousin Centimeters
def Inches_to_Centimeters(inches):
    centimeters=inches * 2.54
    return centimeters
inches=float(input("Enter distance/height in inches: "))
print("distance/height in centimeters")
print(Inches_to_Centimeters(inches))

#A discussions between Centimeters and her cousin Inches
def Centimeters_to_Inches(Centimeters):
        inches=centimeters / 2.54
        return inches 
centimeters=float(input("Enter distance/height in centimeters: "))
print("distance/height in inches")
print(Centimeters_to_Inches(centimeters))

#A discussion between Grams and her aunty Kilograms
def Grams_to_Kilograms(grams):
    kilograms=grams / 1000
    return kilograms
grams=float(input("Enter grams: "))
print("The conversion of grams to kilograms is: ")
print(Grams_to_Kilograms(grams))

#A discussion between Kilograms and her niece Grams  
def Kilograms_to_Grams(Kilograms):
    grams=kilograms * 1000
    return grams 
kilograms=float(input("Enter Kilograms:"))
print("The conversion of Kilograms to grams is: ")
print(Kilograms_to_Grams(kilograms))