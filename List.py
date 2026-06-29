# Practice different list methods and functions in python

# Creating a list
lst1=list(range(1,11))
print(lst1)

#Accessing elements in a list  
print(f"first element in the list is:{lst1[0]}")
print(f"second element in the list is:{lst1[1]}")
print(f"middle element of the list is:{lst1[len(lst1)//2]}")
print(f"last element of the list is:{lst1[-1]}")

#Slicing a list
print(f"first 5 elements of the list are:{lst1[:5]}")
print(f"last 5 elements of the list are:{lst1[-5:]}")
print(f"elements from index 2 to 5 are:{lst1[2:6]}")

#List comprehension
lst2=[x**2 for x in range(1,11)]
print(f"list of squares of first 10 natural numbers is:{lst2}") 

#Filtering a list
evens=[x for x in lst1 if x%2==0]
print(f"the even numbers in the list are:{evens}")

#list methods
import random
random_numbers=[random.randint(1,100) for _ in range(10)]
print(f"random numbers are:{random_numbers}")
print(f"sum of random numbers is:{sum(random_numbers)}")
print(f"maximum number in the list is:{max(random_numbers)}")
print(f"minimum number in the list is:{min(random_numbers)}")  
print(f"sorted list of random numbers is:{sorted(random_numbers)}")
print(f"reversed list of random numbers is:{list(reversed(random_numbers))}")
unique_numbers=list(set(random_numbers))
print(f"unique numbers in the list are:{unique_numbers}")

#nested lists
matrix=[[1,2,3],[4,5,6,[7,8,9]]]
for row in matrix:
    print(row)

#Sorting a list of dictionaries
Student=[{"name":"mohit","score":90},{"name":"rohit","score":80},{"name":"sachin","score":70}]
sorted_students=sorted(Student,key=lambda x:x['score'],reverse=True)
print(f"students sorted by score in descending order are:{sorted_students}")

#flattening a nested list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat_list=[items for sublist in matrix for items in sublist]
print(f"flattened list is:{flat_list}")

#Zipping two lists
names=["mohit","rohit","sachin"]
scores=[90,80,70]
zipped_list=list(zip(names,scores))
print(f"zipped list of names and scores is:{zipped_list}")

#reversing a list
reversed_list=lst1[::-1]
print(f"reversed list is:{reversed_list}")      

#rotating a list
def rotate_list(lst,n):
    return lst[n:]+lst[n:]
n=3  # number of positions to rotate
print(f"list after rotating by {n} positions is:{rotate_list(lst1,n)}")
