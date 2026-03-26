# this is another python program to calulate avg grade 

total=0
grade_count=0

grade=int(input("enter you grade"))

# enter -1 to stop 
while grade!=-1:
    total+= grade
    grade_count+=1
    grade=int(input("enter you grade"))

if grade_count!=0:
    average=total/grade_count
    print(f'average{average:.2f}')
else:
    print('No grade were entered')