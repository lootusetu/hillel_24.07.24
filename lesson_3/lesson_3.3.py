list_1 = [1, 2, 3]
if len(list_1) == 0:
    print([[], []])
else:
    mid = (len(list_1) + 1) // 2
    first_half = list_1[:mid]
    second_half = list_1[mid:]
    print([first_half, second_half])

