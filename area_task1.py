# program to find the area of the circle

# defining the value of pi
pi = 3.14159 
# accepting the radius of the circle from the user 
radius = float(input("Input the radius of the circle: "))
# calculating the area using the formula
area = pi * radius ** 2
# printing the calculated area
print("The area of the circle with radius %.1f is : %f" %(radius,area))