def permutetations(string):# this program is used to find the combination of string
    list=[]
    if len(string)==1:
        list=[string]
    else:
        for i,let in enumerate(string):#acs as iterator
            for j in permutetations(string[:i]+string[i+1:]):#send the character on the left and right of i
                list+=[let+j]
    return list
print(permutetations('abc'))