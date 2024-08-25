my_list = [1, 3, 5]
if not my_list:
    print(0)
else:
    res = []
    for index, element in enumerate(my_list):
        if index % 2:
            continue
        res.append(element)

    print(sum(res)*my_list[-1])

