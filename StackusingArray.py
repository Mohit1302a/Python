def Stack_usingArray():
    stack=[]
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            element=int(input("Enter the element to be pushed:"))
            stack.append(element)
            print("Element pushed successfully")
        elif choice==2:
            if len(stack)==0:
                print("Stack is empty")
            else:
                popped_element=stack.pop()
                print("Popped element is:",popped_element)
        elif choice==3:
            if len(stack)==0:
                print("Stack is empty")
            else:
                print("The elements in the stack are:",stack)
        elif choice==4:
            break
        else:
            print("Invalid choice")
Stack_usingArray()  