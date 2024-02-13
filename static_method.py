class Tempature:
    @staticmethod
    def celcius_to_fahrenheit(c):
        return c * 9/5 + 32
    
    @staticmethod
    def fahrenheit_to_celcius(f):
        return (f - 32) * 5/9
    
# Test
print(Tempature.celcius_to_fahrenheit(32))
print(Tempature.fahrenheit_to_celcius(89.6))