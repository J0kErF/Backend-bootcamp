
def temperature():
    tempType= input('Enter the type of temperature conversion: \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius \n')
    match tempType:
        case '1':
            celsius= float(input('Enter the temperature in Celsius: '))
            fahrenheit= (celsius * 9/5) + 32
            print('The temperature in Fahrenheit is:', fahrenheit)
        case '2':
            fahrenheit= float(input('Enter the temperature in Fahrenheit: '))
            celsius= (fahrenheit - 32) * 5/9
            print('The temperature in Celsius is:', celsius)
        case _:
            print('Invalid input')
            return temperature()

def speed():
    speedType= input('Enter the type of speed conversion: \n 1. KPH to MPH \n 2. MPH to KPH \n')
    match speedType:
        case '1':
            kph= float(input('Enter the speed in KPH: '))
            mph= kph * 0.621371
            print('The speed in MPH is:', mph)
        case '2':
            mph= float(input('Enter the speed in MPH: '))
            kph= mph * 1.609344
            print('The speed in KPH is:', kph)
        case _:
            print('Invalid input')
            return speed()
        
def weight():
    weightType= input('Enter the type of weight conversion: \n 1. KG to Pounds \n 2. Pounds to KG \n 3. KG to Stones \n 4. Stones to KG \n 5. Pounds to Stones \n 6. Stones to Pounds')
    match weightType:
        case '1':
            kg= float(input('Enter the weight in KG: '))
            pounds= kg * 2.20462
            print('The weight in Pounds is:', pounds)
        case '2':
            pounds= float(input('Enter the weight in Pounds: '))
            kg= pounds / 2.20462
            print('The weight in KG is:', kg)
        case '3':
            kg= float(input('Enter the weight in KG: '))
            stones= kg * 0.157473
            print('The weight in Stones is:', stones)
        case '4':
            stones= float(input('Enter the weight in Stones: '))
            kg= stones / 0.157473
            print('The weight in KG is:', kg)
        case '5':
            pounds= float(input('Enter the weight in Pounds: '))
            stones= pounds * 0.0714286
            print('The weight in Stones is:', stones)
        case '6':
            stones= float(input('Enter the weight in Stones: '))
            pounds= stones / 0.0714286
            print('The weight in Pounds is:', pounds)
        case _:
            print('Invalid input')
            return weight()
        
def convertor():
    convertType= input('Enter the type of conversion: \n 1. temperature \n 2. weight \n 3. speed \n')
    match convertType:
        case '1':
            return temperature()
        case '2':
            return weight()
        case '3':
            return speed()
        case _:
            print('Invalid input')
            return convertor()
        
convertor() 