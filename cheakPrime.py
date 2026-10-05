def check_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input("Enter a number: "))
print("The number is prime") if check_prime(n) else print("The number is not prime")

#using this we will gave range of prime numbers between 1 to n
print("The prime numbers between 1 and",n,"are:")
for i in range(1,n+1):
    if check_prime(i):
        print(i,end=" ")
