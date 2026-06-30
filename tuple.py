#1 Creating a tuple
mht=tuple(range(1,11))
print(mht)

#2 Accessing elements in a tuple
print(f"first element is {mht[0]}")
print(f"second element is {mht[1]}")
print(f"middle element is {mht[len(mht)//2]}")
print(f"last element is {mht[-1]}")

#3 Slicing a tuple
print(f"first 5 elements are {mht[:5]}")
print(f"last 5 elements are {mht[-5:]}")
print(f"element from index 2 to 6 are:{mht[2:6]}")

#4 Tuple comprehension
# Note: Tuples do not support comprehension directly, but we can create a tuple from a list comprehension
mht_squares=tuple(x**2 for x in range(1,11))
print(f"tuple of squares of first 10 natural numbers is:{mht_squares}") 

#5 tuple concatenation
mht1=(1,2,3)
mht2=(4,5,6)
mht3=mht1+mht2
print(f"concatenated tuple is:{mht3}")

#6 tuple methods
mht4=(1,2,2,3,3,4,4,5,5,5,5)
print(f"count of 5 in tuple is:{mht4.count(5)}")
print(f"index of first occurrence of 2 in tuple is:{mht4.index(2)})")

#7 unpacking a tuple
mht5=(1,2,3)
a,b,c=mht5
print(a,b,c)

#8 nested tuples
nested_tuple=((1,2,3),(4,5,6))  

#9 tuple and string
String="Mohit is a programmer"
mht6=tuple(String)
joined_string=''.join(mht6)
print(f"{joined_string}")



