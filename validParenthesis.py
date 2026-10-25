def parenthesis(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
print("Enter a string containing parentheses:")
input_string = input()
if parenthesis(input_string):
    print("The parentheses in the string are valid.")
else:
    print("The parentheses in the string are not valid.")