stack = []
top=-1
def push():
    dt=input("Enter data type (Int, str): ")
    if dt == "Int":
        element = int(input("Enter the element to push: "))
    elif dt == "str":
        element = input("Enter the element to push: ")
    else:
        print("Invalid data type")
        return
    stack.append(element)
    top+=1
    print(f"{element} pushed to stack")
    print(f"Current stack: {stack}")
    print(f"Stack size: {len(stack)}")
    print(f"Top element: {stack[0]}")
    print(f"top: {top}")
def pop():
    if not stack:
        print("Stack is empty")
    else:
        element = stack.pop()
        top=-1
        print(f"{element} popped from stack")
        print(f"Current stack: {stack}")
        print(f"Stack size: {len(stack)}")
        print(f"Top element: {stack[0]}")
        print(f"top: {top}")
def peek():
    if not stack:
        print("Stack is empty")
    else:
        print(f"Top element is {stack[0]}")
def display():
    if not stack:
        print("Stack is empty")
    else:
        print(f"Current stack: {stack}")
        print(f"Stack size: {len(stack)}")
        print("Stack elements are: ")
        for element in stack:
            print(element)
while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, please try again.")