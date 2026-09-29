def Even_odd_diffrence(nums):
    even_sums=0
    odd_sums=0
    for i in range(len((nums))):
        if nums[i]%2==0:
            even_sums+=nums[i]
        else:
            odd_sums+=nums[i]
    return even_sums-odd_sums

nums=list(map(int,input("Enter the numbers").split()))
print("The diffrence between the sum of even and odd numbers is:",Even_odd_diffrence(nums))
