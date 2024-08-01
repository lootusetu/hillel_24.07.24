#HT №1
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

#HT №2
number_2 = int(input("Enter a 5-digit number: "))
number_2 = int(number_2)

number1 = number_2 // 10000
number2 = (number_2 % 10000) // 1000
number3 = (number_2 % 1000) // 100
number4 = (number_2 % 100) // 10
number5 = number_2 % 10

result = number5 * 10000 + number4 * 1000 + number3 * 100 + number2 * 10 + number1
print(result)