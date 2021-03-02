#insertion sort
def insertion_sort(lst):
    for sliceend in range(len(lst)):
        #build longer and longer sorted slices
        #in each iteration lst[0:sliceend] already sorted
        #move first element after sorted slice left till it is the correct place
        pos=sliceend
        while pos>0 and lst[pos] < lst[pos-1]:
            lst[pos],lst[pos-1]=lst[pos-1],lst[pos]
            pos=pos-1

lst=[]
num=int(input("how many no you want to enter "))
print("enter the num")
for i in range(num):
    lst.append(int(input()))
insertion_sort(lst)
print(lst)