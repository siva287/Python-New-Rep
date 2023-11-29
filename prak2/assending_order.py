my_list = [26, 14, 24, 13, 5]
for i in range(0, len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] >= my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)

my_list2 = [26, 14, 12, 18, 21, 24, 13, 5]
for i in range(0, len(my_list2)):
    for j in range(i+1, len(my_list2)):
        if my_list2[i] > my_list2[j]:
            tem = my_list2[i]
            my_list2[i] = my_list2[j]
            my_list2[j] = tem

print(my_list2)

my_list3 = [26, 14, 12, 18, 21]
my_list3.sort()
print(my_list3)
