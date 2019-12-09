def primeFactors():
    num=int(input("enter a number to find the factors:"))
    for i in range(2,num):
        if (num%i)==0:
            print(i)
            num=num/i
primeFactors()