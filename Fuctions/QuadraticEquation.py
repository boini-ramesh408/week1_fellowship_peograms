from com.bridgelabz.python.utility.pythonUtil import quadraticEquation
try:
    a=float(input("enter a value:"))
    b=float(input("enter b value:"))
    c=float(input("enter c value:"))

    quadraticEquation(a,b,c)
except ValueError:
    print("enter only numberss to fing the roots")
