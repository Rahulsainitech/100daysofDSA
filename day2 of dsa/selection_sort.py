# selection sort algorithm
def selection_sort(arr):
    for start in range(len(arr)):
        minpos=start
        for i in range(len(arr)):
            if arr[i]>arr[minpos]:
                arr[minpos],arr[i]=arr[i],arr[minpos]

a=[2,46,3,52,25,62,]
selection_sort(a)
print(a)