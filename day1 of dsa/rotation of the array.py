a=[1,2,3,4,5,6,7,8,9]
# rotation of the array
def left_rotation_by_one(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
def left_rotation(arr,n,d):
    for i in range(d):
        left_rotation_by_one(arr,n)
left_rotation(a,9,2)
print(a)