my_list = [12, 3, 4, 10, 8]
if len(my_list) <= 1:
    print(my_list)
else:
    last_element = my_list.pop()
    my_list.insert(0, last_element)
    print(my_list)