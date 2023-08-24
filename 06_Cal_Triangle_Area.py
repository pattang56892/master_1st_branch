# print('Please input three numbers: ')  # three sides of a triangle
# x = float(input(''))
# y = float(input(''))
# z = float(input(''))
# print('%f ' %x)
# print('%f ' %y)
# print('%f ' %z)
# # calculate the half girth
# girth = (x + y + z) / 2
# # calculate the triangle area
# area = (girth*(girth-x)*(girth-y)*(girth-z)) ** 0.5
# print('The triangle area is: %0.3f' %area)


print('Please input three numbers: ')  # three sides of a triangle
numbers = input('').split()  # Split the input into a list of strings
x = float(numbers[0])  # Convert the first string to float
y = float(numbers[1])  # Convert the second string to float
z = float(numbers[2])  # Convert the third string to float
print('%0.2f ' % x)
print('%0.2f ' % y)
print('%0.2f ' % z)
# calculate the half girth
girth = (x + y + z) / 2
# calculate the triangle area
area = (girth * (girth - x) * (girth - y) * (girth - z)) ** 0.5
print('The triangle area is: %0.2f' % area)
