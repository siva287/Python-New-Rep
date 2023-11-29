my_list = [26, 15, 26, 13, 18, 16, 16, 14, 24, 13, 5]
for i in range(0, len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] == my_list[j]:
            print(my_list[i])
