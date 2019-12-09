from com.bridgelabz.python.utility.pythonUtil import array2D
try:
    rows = int(input("enter row size :"))
    col = int(input("enter column size:"))
    array2D(rows,col)
except ValueError:
    print("enter row and column values in Integer")

