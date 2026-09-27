def rotate_list(input_array,k):
    n=len(input_array)
    k=k%n
    return input_array[-k:]+input_array[:-k]
input_array=list(map(int,input("Enter the elements of the array separated by space: ").split()))
k=int(input("Enter the number of rotations: "))
print("The rotated list is:",rotate_list(input_array,k))    