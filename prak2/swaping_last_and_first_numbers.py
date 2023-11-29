my_list = [16, 14, 24, 13, 5, 27]

# my_list[0], my_list[len(my_list)-1] = my_list[len(my_list)-1], my_list[0]
# print(my_list)

temp= my_list[0]
my_list[0] = my_list[len(my_list)-1]
my_list[len(my_list)-1] = temp

print(my_list)



