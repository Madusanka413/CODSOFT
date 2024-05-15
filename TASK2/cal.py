def calculator():
    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user to choose an operation
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Perform the chosen operation and display the result
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please select a valid option (1/2/3/4).")

# Call the calculator function to run the program
calculator()