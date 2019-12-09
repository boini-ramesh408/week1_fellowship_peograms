from com.bridgelabz.python.utility.pythonUtil import windChill
try:
    temparature=float(input("enter temparature value:"))
    velocity=float(input("enter speed value:"))
    windChill(temparature,velocity)
except ValueError:
    print("enter only number to find temparature and speed")