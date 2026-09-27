def countEvenOdd(input):
    even_count=0
    odd_count=0
    for i in input:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    return {"even_count":even_count,"odd_count":odd_count}
input=list(map(int,input("enter the numbers: ").split()))
print("the count of even and odd numbers is:",countEvenOdd(input))
