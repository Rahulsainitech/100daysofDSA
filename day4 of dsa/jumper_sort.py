import math
def jump_sort(arr,n,x):
    step=math.sqrt(n)
    prev=0
     # Doing a linear search for x in  
    # block beginning with prev. 
    while (arr[int(min(step,n)-1)]<x):
        prev=step
        step+=math.sqrt(n)
        if prev>n:
            return -1
    while arr[int(prev)]>x:
        prev+=1
        # If we reached next block or end  of array, element is not present. 
        if prev == min(step, n): 
            return -1
    if arr[int(prev)]==x:
        return prev
    return-1
# driver code 
arr=[1,2,3,4,5,6,7,8,9,10]
n=len(arr)
x=10
# function call
result=jump_sort(arr,n,x)
if result==-1:
    print("element is not in list")
else:
    print("the element is at index ",result)