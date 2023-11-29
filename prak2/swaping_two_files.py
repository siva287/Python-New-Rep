num1 = input("enter num1 value:" )
num2 = input("enter num2 value:" )

temp = num1
num1 = num2
num2 = temp

print(num1, num2)

num3 = 30
num4 = 40
num3, num4 = num4, num3
print(num3, num4)


