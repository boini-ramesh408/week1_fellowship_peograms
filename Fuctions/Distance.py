from com.bridgelabz.python.utility.pythonUtil import main
try:
    x=int(input("enter x value:"))#taking integer value as input
    y=int(input("enter y value:"))
    main(x,y)
except ValueError:
    print("enter only integer values to find the distance and power")