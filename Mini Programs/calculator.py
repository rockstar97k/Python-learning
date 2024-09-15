# Calculator program

num1 = float(input("Enter value for num1:"))
num2 = float(input("Enter value for num2:"))
choice = input("Enter your operation + - * /")

# Create an array of valid operators
valid_operators = ["+", "-", "*", "/"]

# Check if the choice is in the array
if choice in valid_operators:
    # Perform the corresponding operation
    if choice == "+":
        sum = num1 + num2
        print(sum)
    elif choice == "-":
        diff = num1 - num2
        print(diff)
    elif choice == "*":
        multiply = num1 * num2
        print(multiply)
    else:  # choice must be "/"
        divide = num1 / num2
        print(divide)
else:
    print("Invalid choice")