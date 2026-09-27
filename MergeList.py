def merge_list(l1, l2):
    i=0
    j=0
    merged_list=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            merged_list.append(l1[i])
            i+=1
        else:
            merged_list.append(l2[j])
            j+=1
    while i<len(l1):
        merged_list.append(l1[i])
        i+=1
    while j<len(l2):
        merged_list.append(l2[j])
        j+=1
    return merged_list
l1=list(map(int,input("Enter the elements of the first array separated by space: ").split()))
l2=list(map(int,input("Enter the elements of the second array separated by space: ").split()))
print("The merged list is:",merge_list(l1,l2))