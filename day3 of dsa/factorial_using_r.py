#factorial of a number using recursive method 
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*factorial(n-1))
num= int(input("enter the number "))
print("factorial of the number",factorial(num))