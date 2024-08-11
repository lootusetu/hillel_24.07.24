list_1 = []
if len(list_1) == 0:
    print([[], []])

list_2 = [1, 2, 3, 4, 5, 6]
mid = (len(list_2)) // 2

first_half = list_2[:mid]
second_half = list_2[mid:]

result_list2 = [first_half, second_half]
print(result_list2)

list_3 = [1]
mid = (len(list_2) + 1) // 2

first_half = list_3[:mid]
second_half = list_3[mid:]

result_list3 = [first_half, second_half]
print(result_list3)