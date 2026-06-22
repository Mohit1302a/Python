# simple calculator
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
if operation=='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
elif operation=='/':
    if num2!=0:
        result=num1/num2
    else:
        result="Error! Division by zero."
print("Result:", result)


#calulate number of prime numbers in a given range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num>1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')