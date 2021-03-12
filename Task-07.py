def convert_to_fahrenheit(celsius):
    fahren = celsius * 9/5 + 32
    return ("{}C = {}F".format(celsius, fahren))

def convert_to_celsius(fahrenheit):
    cels = (fahrenheit - 32)/1.8
    return ("{}F = {}C".format(fahrenheit, cels))
    
print(convert_to_fahrenheit(20))
print(convert_to_celsius(68))