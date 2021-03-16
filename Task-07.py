def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32      
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8    
    return celsius
    
print(convert_to_fahrenheit(20))
print(convert_to_celsius(68))

