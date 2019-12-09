from com.bridgelabz.python.utility.pythonUtil import decimal_to_binary
try:
    number = int(input("enter a decimal number to convert binary:"))
    decimal_to_binary(number)
except ValueError:
    print("enter only decimal numbers")
