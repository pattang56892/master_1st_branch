print('Please input a radius: ')
radius = float(input(''))
print('%0.2f ' % radius)
def area(r): 
    PI = 3.142
    return PI * (r*r)
print("The area of circle is: %.2f" %area(radius))