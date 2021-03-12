def convert_to_fahrenheit(celsius):
    fahren = celsius * 9/5 +32
    return (celsius + 'C = ' + fahren + 'F')

def convert_to_celsius(fahrenheit):
    cels = (fahrenheit - 32)/1.8
    return (fahrenheit + 'F = ' + cels + 'C')
    
print(convert_to_fahrenheit(20))
print(convert_to_celsius(68))