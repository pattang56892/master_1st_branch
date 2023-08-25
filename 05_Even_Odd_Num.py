number = float(input("Please input a number: "))
print(number)
if (number % 2) == 0:
    print("{0} is an even number.".format(number))
else:
    print("{0} is an odd number.".format(number))