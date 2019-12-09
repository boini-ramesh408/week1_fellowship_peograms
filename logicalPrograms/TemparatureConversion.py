from com.bridgelabz.python.utility.pythonUtil import temparatue_conversion
try:

    celsius = float(input("enter Celsius to convert Fahrenheit:"))
    fahrenheit = float(input("enter Fahrenheit to convert celsius:"))
    temparatue_conversion(celsius, fahrenheit)
except:
    print("enter only float values")
