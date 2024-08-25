my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zeros = []
for element in my_list:
    if element != 0:
        non_zeros.append(element)

zeros = [0] * my_list.count(0)

print(non_zeros + zeros)




