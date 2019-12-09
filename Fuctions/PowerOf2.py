from com.bridgelabz.python.utility.pythonUtil import power_of_2
try:

    nValue = int(input("enter n value:"))
    power_of_2(nValue)
except ValueError:
    print("enter only numbers")

