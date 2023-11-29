my_list = [1, 6, 3, 5, 3, 6, 4]
ele = 3
flag = 0
for i in my_list:
    if i == ele:
        print("element found")
        flag = 1
        break
    if flag==0:
        print("not found")
