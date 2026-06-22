## factorial of a number 
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

## fibonacci series
num2 = int(input("Enter the number for fibonacci series: "))
a=0
b=1

for i in range(num2):
    print(a, end=' ')
    a, b = b, a+b

## check if a number is prime
num3 = int(input("Enter a number to check if it is prime: "))
if num3 > 1:
    for i in range(2,num3):
        if num3%i==0:
            print(num3,"is not a prime number")
            break
    else:     print(num3,"is a prime number")       

## check if a number is even or odd
num4 =int(input("Enter a number to check if it is even or odd: "))
if num4%2==0:
    print(num4,"is an even number")
else:
    print(num4,"is an odd number")

##swap two numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)       

## square of a number
num5 = int(input("Enter a number to find its square: ")) 
print("Square of", num5, "is", num5**2)
