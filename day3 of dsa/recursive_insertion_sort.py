
# recursive insertion sort
def insertion_sort_r(lst,n):
   if n<=1:
        return 
   insertion_sort_r(lst,n-1)
   last=lst[n-1]
   j=n-2
    
   while (j>=0 and lst[j]>last):
        lst[j+1]=lst[j]
        j=j-1
   lst[j+1]=last

lst=[4,5,6,6,3,5,6,2,4,66,77,54,4,5,6]
n=len(lst)
insertion_sort_r(lst,n)
print(lst)