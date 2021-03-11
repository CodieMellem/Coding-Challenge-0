def convert_to_fahrenheit(celsius):
    fahren = celsius * 9/5 +32
    return fahren

def convert_to_celsius(fahrenheit):
    cels = (fahrenheit - 32)/1.8
    return cels
    
print(convert_to_fahrenheit(20))
print(convert_to_celsius(68))