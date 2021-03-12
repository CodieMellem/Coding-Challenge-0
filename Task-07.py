def convert_to_fahrenheit(celsius):
    fahren = celsius * 9/5 + 32      #Formula for converting fahrenheit to celsius
    return ("{}C = {}F".format(celsius, fahren))

def convert_to_celsius(fahrenheit):
    cels = (fahrenheit - 32)/1.8     #Formula for converting Celsius to fahrenheit
    return ("{}F = {}C".format(fahrenheit, cels))
    
print(convert_to_fahrenheit(20))
print(convert_to_celsius(68))

"""
need more feedback on what type of changes
are needed to make this code more understandable
"""