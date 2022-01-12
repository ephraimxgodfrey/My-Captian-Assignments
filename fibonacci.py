# program to print a fibonacci series

# initializing varaibles for the first and second elements of the series
first = 0
second = 1
# getting the size of the series from the user
s = int(input("Enter the size of the series: ")) 
# for keeping track of iteration
count = 0
# specifying an error message for invalid size
if s <= 0:
    print("Please enter a positive integer")
# printing only the first element when the size is 1
elif s == 1:
    print(first)
#printing the series for a size greater than 1
else:
    count = count + 2
    print("Fibonacci Series: ")
    print(first)
    print(second)
    while count < s:
        third = first + second
        print(third)
# updating values
        first = second 
        second = third
        count = count + 1