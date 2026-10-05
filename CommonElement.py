def Common_element(list1,list2):
    common=[]
    for i in list1:
        if i in list2:
            common.append(i)
    return common
list1=list(map(int,input("enter ").split()))
list2=list(map(int,input("enter ").split()))
common=Common_element(list1,list2)
if len(common)==0:
    print("no common elements")
else:
    print("The common elements are:",common)