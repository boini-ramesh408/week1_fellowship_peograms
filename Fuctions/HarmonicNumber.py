from com.bridgelabz.python.utility.pythonUtil import harmonic_number
try:
    nthValue=int(input("enter Nth value"))
    harmonic_number(nthValue)
except ValueError:
    print('enter only numberss')


