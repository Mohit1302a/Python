def max_diff(arr):
    if len(arr)<2:
        return 0
    maxdiff=0
    for i in range(len(arr)-1):
        diff=abs(arr[i]-arr[i+1])
        if diff>maxdiff:
            maxdiff=diff
    return maxdiff
arr=list(map(int,input("Enter the elements of the array separated by space: ").split()))
print("The maximum difference between two consecutive elements of the array is:",max_diff(arr))