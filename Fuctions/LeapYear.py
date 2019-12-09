from com.bridgelabz.python.utility.pythonUtil import CheckingLeapYear

try:
    year = int(input("enter a year:"))
    CheckingLeapYear(year)
except ValueError:
    print("enter only valid years..")
