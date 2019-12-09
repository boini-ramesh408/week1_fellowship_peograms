
pos =-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:#always l is less than u
        mid=(l+u)//2#// gives the integer division
        if list[mid]==n:# if mid value and thesearching value are equal it returns true
          globals()['pos']=mid
          return True
        else:
            if list[mid]<n:
                l=mid+1#if mid value is lessthan n the values increases by 1
            else:
                u=mid-1#if mid value greater than n then value decreases by 1
        return  False
list=["abc","dfk","fghh"]
n="dfk"
if search(list,n):
    print("found",pos+1)#pos is used to fing the position of the word in the list
else:
    print("not found")
