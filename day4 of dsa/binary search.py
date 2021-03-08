#binary search
def binary_search(lst,l,r,x):
    while l<=r:
        mid =l + (r-1) //2
        # Check if x is present at mid 
        if lst[mid] == x:
            return mid
            # If x is greater, ignore left half 
        elif lst[mid]<x:
            l=mid+1 
        # If x is smaller, ignore right half
        else:
            r=mid-1
    else:
        return -1

# driver code 
lst=[1,4,5,6,8]
x=8
result=binary_search(lst,0,len(lst)-1,x) 
if result == -1:
    print("element %d is not in lst"%x)
else:
    print("element {} is at {} index".format(x,result))
    # Python3 code to implement iterative Binary 
# Search. 

# It returns location of x in given array arr 
# if present, else returns -1 
# def binarySearch(arr, l, r, x): 

# 	while l <= r: 

# 		mid = l + (r - l) // 2
		
# 		# Check if x is present at mid 
# 		if arr[mid] == x: 
# 			return mid 

# 		# If x is greater, ignore left half 
# 		elif arr[mid] < x: 
# 			l = mid + 1

# 		# If x is smaller, ignore right half 
# 		else: 
# 			r = mid - 1
	
# 	# If we reach here, then the element 
# 	# was not present 
# 	return -1

# # Driver Code 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 40

# # Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 

# if result != -1: 
# 	print ("Element is present at index % d" % result) 
# else: 
# 	print ("Element is not present in array") 
