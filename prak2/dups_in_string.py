str = "sivaisaas"
list1=list(str)

for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] == list1[j]:
            print(list1[i])
