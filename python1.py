# Program for counting the no of passed and failed subject for a student 

passes=0
failure=0

for student in range(10):

    result=int(input('Enter a number 1=pass,2= fail '))

    if result==1:
        passes=passes+1
    else:
        failure=failure+1
print('Passed in:',passes)
print('failed in:',failure)

if passes>8:
    print("good performane")
