my_list = [16, 14, 24, 13, 5, 27]
max = my_list[0]
for i in range(1, len(my_list)):
    if max < my_list[i]:
        max = my_list[i]
print(max)


#minimun value
for i in range(1, len(my_list)):
    if my_list[i] < max:
        max = my_list[i]
print(max)


