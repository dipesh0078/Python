#34.Use a lambda function with map() to convert a list of temperatures from Celsius to Fahrenheit.

convert= lambda lst:list(map((lambda c: c*9/5+32),lst))

celsius_temps = [0, 20, 37, 100]

print(convert(celsius_temps))