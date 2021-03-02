#bubble sort algorithm
def bubble_sort(lst):
    for j in range(len(lst)-1):
        for i in range(j):
            print(lst)
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
        print()

lst=[4,3,2,5,6,7]
# num=int(input("how many number you want to enter"))
# for i in range(num):
#     lst.append(int(input()))

bubble_sort(lst)
print(lst)

