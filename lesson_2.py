number = input("Enter a 4-digit number: ")
number = int(number)

first_number = (number // 1000)
second_number = (number % 1000) // 100
third_number = (number % 100) // 10
fourth_number = number % 10


print(first_number)
print(second_number)
print(third_number)
print(fourth_number)