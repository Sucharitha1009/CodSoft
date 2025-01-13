def calculator():
    operations = {
        '1': lambda x, y: x + y,
        '2': lambda x, y: x - y,
        '3': lambda x, y: x * y,
        '4': lambda x, y: x / y if y != 0 else "Error! Division by zero."
    }

    print("Welcome to the Simple Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice in operations:
            result = operations[choice](num1, num2)
            print(f"The result of {num1} {['+', '-', '*', '/'][int(choice) - 1]} {num2} is: {result}")
        else:
            print("Invalid operation choice. Please select a valid option.")

        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            break

calculator()