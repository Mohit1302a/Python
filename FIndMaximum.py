def max_sum_diff(nums):
    max_sum=0
    max_diff=0
    for i in range(len(nums)):
        if nums[i]>0:
            max_sum+=nums[i]
        else:
            max_diff+=abs(nums[i])
    return max_sum,max_diff
nums=list(map(int,input("Enter the numbers").split()))
max_sum,max_diff=max_sum_diff(nums)
print("The sum of positive numbers is:",max_sum)
print("The sum of absolute values of negative numbers is:",max_diff)