def check_subset(arr1,arr2):
    set1=set(arr1)
    set2=set(arr2)
    return set2.issubset(set1)
arr1=list(map(int,input("enter the elemnts of the first array separated by space: ").split()))
arr2=list(map(int,input("enter the elemnts of the second array separated by space: ").split())) 
print("the second array is a subset of the first array:",check_subset(arr1,arr2))
