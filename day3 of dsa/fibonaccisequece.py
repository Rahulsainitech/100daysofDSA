#fibonaci sequence suing recursion method
def fibo(n):
    if n==0 :
        return 0
    if  n==1 or n==2:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))


num=int(input("no of fibbonacci sequence you want"))
for i in range(num):
    print(fibo(i),end=' ')