#########################Basic core programs###########################
# string template program
import time


def string_template(username):
    text = "hii <<userName>> ,how are you"  # hii ramesh how are you
    result = re.sub("<<userName>>", username,
                    text)  # replace fuction has two arguments...in this first argument is replaced by the second argument
    print(result)


# -----------------------------------------------
# finding heads and tails percentage
import random

def Heads_or_tails_percentage(noOfTimes):
    heads = 0
    tails = 0
    r = random.random()  # this function is used for generating the 0 and 1 values
    if (r > 0.5):  # probability is between 0 and 1...so if it is greater than 0 then it is heads or it is tails
        print("Heads")
        headsCount = heads + 1  # or heads+=1
        print("heads count is", headsCount)  # print how many times head occuring
        headp = headsCount / noOfTimes * 100  # to find pecentage of heads
        print("heads percentage is", headp)
        tailsCount = noOfTimes - headsCount
        print("tails count is", tailsCount)
        tailp = 100 - headp
        print("tails percentage is", tailp)


# ----------------------------------------------------
# leap year program
def CheckingLeapYear(year):
    if (year % 4) == 0 or (year % 400) == 0:
        print("yes it is a leap year")
    else:
        print("it is not a leap year")


# -------------------------------------------------------
# power of 2 program
def power_of_2(nValue):
    power = 1
    num = 0
    while (nValue >= num) and (nValue <= 31):
        print(power)
        power = power * 2  # power=math.pow(2,nValue)
        num = num + 1

# --------------------------------------------------------
# harmonic number program
def harmonic_number(nthValue):
    harmonic = 0
    for i in range(1, nthValue):
        harmonic = harmonic + 1 / i
        print(harmonic)


# ********************Functional Programs************************
# Array 2D program...
def array2D(rows, col):
    list = []
    for i in range(rows):  # this lopp creats the empty array based on inputs with o values
        list.append([0] * col)  # for every row it creaes colums(all ex 3)
    for i in range(rows):  # this loop is for read the input from user
        for j in range(col):
            list[i][j] = int(input("enter the row value " + str(i + 1) + "  and enter column value " + str(j + 1) + ":"))
    for i in range(rows):  # this loop is used to print the values
        for j in range(col):
            print(list[i][j], end=" ")
        print()  # if we are not usig this print statement...the output will peints only in one line

# -----------------------------------------------------------------
# sum of three integers is equal to zero program
def sum_of_threeInteger(array):
    # a=[1,5,8,-4,-2,-1,4]
    for i in range(0, len(array)):  # ut takes 1st element
        for j in range(1, len(array)):  # it takes secong element
            for k in range(2, len(array)):  # it takes third element
                if (array[i] + array[j] + array[k]) == 0:
                    print(array[i], " ", array[j], " ", array[k])

# -----------------------------------------------------------------
# distance program
import math


def main(x, y):
    distance = math.sqrt(x * x + y * y)  # formula for finding the distance
    power = math.pow(x, y)  # formula for finding the power
    print("distance is", distance)
    print("power is", power)


# ----------------------------------------------------------------
# Quadratic uquation progrm
import cmath


def quadraticEquation(a, b, c):
    determinant = (b ** 2) - (4 * a * c)
    root1 = (-b + cmath.sqrt(determinant)) / (2 * a)
    root2 = (-b - cmath.sqrt(determinant)) / (2 * a)
    print("root 1 is", root1, "root 2 is", root2)


# ----------------------------------------------------------------
# windChill program
def windChill(t, v):
    wind = 0.0
    if (t < 120 and t > 3) and (v < 50):#it checks the condition
        wind = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    print(wind)


# ---------------------------------------------------------------------
###########################logical Programss+#########################
# Gambler program
import math

def gambler(stake, goal, trials):  # pending

    bets = 0
    wins = 0
    for i in range(1, trials):
        cash = stake
        while (cash > 0 and cash <= goal):
            bets = bets + 1
            if math.random() < 0.5:
                cash = cash + 1
            else:
                cash = cash - 1
        if cash == goal:
            wins = wins + 1
    # print(wins+"winning of"+trials)
    winningpercentage = wins / trials * 100
    print(winningpercentage)
    print(100 - winningpercentage)


# ----------------------------------------------------------------
# Coupon Numbers
import random


def Coupon_Number(code_chars):
    code = ''
    for i in code_chars:
        start = random.randint(0, len(code_chars) - 1)
        code += code_chars[start:start + 1]

    print(code)


# --------------------------------------------------------------

# ----------------------------------------------------------------
#######################ALGORITHM PROGRAMS##########################

# Binary search for word from word list
pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:  # always l is less than u
        mid = (l + u) // 2  # // gives the integer division
        if list[mid] == n:  # if mid value and thesearching value are equal it returns true
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1  # if mid value is lessthan n the values increases by 1
            else:
                u = mid - 1  # if mid value greater than n then value decreases by 1
        return False


# ------------------------------------------------------------
# insertion sort
def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:  # if i value lessthan j then swap the elements
            list[j + 1] = list[j]  # move first position to second position
            list[j] = temp
            j = j - 1
    print(list)

# ---------------------------------------------------------------
# Bubble sort
def bubble_sort(list):  # compare to all sorting techniques bubble sorting is very easy
    for i in range(len(list) - 1, 0, -1):  # here iam taking the values max to zero
        for j in range(i):
            if list[j] > list[j + 1]:  # it checks the condition
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

    return  list


# ----------------------------------------------------------------
# anagram program
def anagram(string1, string2):
    sort_str1 = sorted(string1)  # here the sorted function converts the string into alphabetical order
    sort_str2 = sorted(string2)
    if sort_str1 == sort_str2:
        print("it is anagram...")
    else:
        print("not anagram....")


# -----------------------------------------------
# prime numbers program
def primeNumber(n):
    # num=int(input("enter maximun numbers:"))
    arr = []
    for i in range(2, n):  # here iam taking starting values is 2,because prime numbers start from 2
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count = count + 1
                break
        if count == 0:  # here count is 0 because iam not dividing the number with 1 and itself,if i divide the number by one and itself then the count is 2
            print("prime number:", i)



# ------------------------------------------------------

# Regular Expression program....
import re  # re(regular expresssion) is the inbilt module
import datetime


def regEx():
    text = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx.\
    Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
    name = str(input("enter name:"))
    if not name.isalpha():  # isaplha takes only alphabets it is acts like a try block
        name = input("enter name in alphabets:")
    result = re.sub(r"<<name>>", name, text)  # sub function has three argument..it is used to replace the name in text
    # print(result)
    fullName = input("enter fullname")
    if not fullName.isalpha():  # isaplha takes only alphabets it is like ats like a try block
        fullName = input("enter fullName in alphabets:")
    result = re.sub(r"<<full name>>", fullName,
                    result)  # we should give result as a third argument because in resukt name is already replaced
    # print(result)
    contactNo = (input("enter contact number:"))
    if not contactNo.isnumeric():
        contactNo = input("enter contact number in numerics:")
    result = re.sub("xxxxxxxxxx", contactNo, result)
    # print(result)
    datee = datetime.date.today()  # daretime and date and today all are inbuilt functions
    replacedate = str(datee)
    result = re.sub("01/01/2016", replacedate, result)
    print(result)


# ------------------------------------------------------------------------
##########################Program for j unit testing##################
# program for vemding machine

def vending_machine(amount):
    notes = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 1]
    notes_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, j in zip(notes, notes_count):
        if amount > i:
            j = amount // i
            amount = amount - j * i
            print(i, ":", j)

# --------------------------------------------------------------------------
# decimal to binary conversion
def decimal_to_binary(number):
    if number > 1:
        decimal_to_binary(number // 2)  # i generates the quotienet and // is used to generate integer output
    print(number % 2, end=" ")  # if we use % it generates remander output


# -------------------------------------------------------------------------
# temparature cnversion
def temparatue_conversion(celsius, fahrenheit):
    celsius_to_Fahrenheit = (celsius * 9 / 5) + 32  # statement is used to convert celsius to fahrenheit
    fahrenheit_to_celsius = (fahrenheit - 32) * 5 / 9  # statement is used to convert hahenreit to celsius
    print("after converting celisius to fahrenheit is:", celsius_to_Fahrenheit)
    print("after converting fahrenheit to celsius is:", fahrenheit_to_celsius)

# -----------------------------------------------------------------------------