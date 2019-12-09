from com.bridgelabz.python.utility.pythonUtil import sum_of_threeInteger
array=[]
try:
    num=int(input("enter the number:::"))
    for i in range(0,num):#this loop is used for taking the run time values
        elements = int(input("enter the elements"))#it displays what are the elements you are entering
        array.append(elements)
    sum_of_threeInteger(array)
except:
    print("values only")

