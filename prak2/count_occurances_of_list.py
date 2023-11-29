my_list = [16, 14, 24, 13, 5, 27, 16, 10 ,16]
# x = 16
# count = 0
#
# for ls in my_list:
#     if ls == x:
#         count = count + 1
# print("{} has occured {} times".format(x, count))
# second
# print("{} has occured {} times".format(x, my_list.count(x)))
from collections import Counter
dic = Counter(my_list)
print(dic)
