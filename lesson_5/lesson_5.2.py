while True:
    num1 = float(input("Enter: first number "))
    num2 = float(input("Enter: second number "))
    operation = input("Enter: operation +,-,*,/ ")

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by 0!")
        else:
            print(num1 / num2)
    continue_calculation = input("Do you want to continue?  (yes/y to continue): ").lower()
    if continue_calculation not in ['yes', 'y']:
        break

