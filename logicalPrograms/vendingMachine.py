from com.bridgelabz.python.utility.pythonUtil import vending_machine
try:
    amount=int(input("enter amount for printing the notes...."))
    vending_machine(amount)
except ValueError:
    print("enter only numbers")



