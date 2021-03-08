
# time complexity of lineat search is o(n)
# #i=temporary pointer
#x is the number that we have found
# is the length of the array
def sequential_search(lst,x,n):
   i=0
   for i in range(len(lst)):
       if lst[i]==x:
          return print("the element {} is present at {} index values".format(x,i))
       else:
          return print("the element{} is not present in list".format(x))
lst=[1,4,6,78,6,5,74,7,5,7,66,5,6,66,4,643,2,3,7,65778,66,7,6]
sequential_search(lst,6,len(lst))