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

