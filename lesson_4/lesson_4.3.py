import random

num_elements = random.randint(3, 10)
my_list = [random.randint(1, 10) for _ in range(num_elements)]
print(my_list)

selected_elements = [my_list[0], my_list[2], my_list[-2]]

print(selected_elements)

