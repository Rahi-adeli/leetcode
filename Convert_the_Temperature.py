celsius = 36.50

def convertTemperature(celsius):
    ans = []
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00

    ans.extend([kelvin, fahrenheit])
    return ans


result = convertTemperature(celsius)
print (result)