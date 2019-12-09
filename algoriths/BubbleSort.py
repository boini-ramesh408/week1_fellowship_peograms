from com.bridgelabz.python.utility.pythonUtil import bubble_sort
list=[]#to take run time values in sorting first take one emply list and add the elements to the empty list
try:
    num=int(input("enter the number"))
    for i in range(0,num):
        element = int(input())
        list.append(element)
    bubble_sort(list)
except ValueError:
    print("enter only integer values....")


