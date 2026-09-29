def MOve_zero_end(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<len(arr):
        arr[count]=0
        count+=1
    return arr
arr=list(map(int,input("Enter numbers separated by Space:").split()))
print("The array after moving zeros to the end is:",MOve_zero_end(arr)) 