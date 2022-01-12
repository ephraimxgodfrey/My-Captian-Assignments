#  program to print all positive numbers in a range

# making two lists for input and output
myList1 = []
myList2 = []
myOutput1 = []
myOutput2 = []
# getting the size of the list from the user
s1 = int(input("Enter the size of the list1: "))
s2 = int(input("Enter the size of the list2: "))
# specifying an error message for invalid size
if s1 < 0:
    print("Enter a valid size")
else:
    print("Input List1 : ")
    for i in range(0,s1):
        ele = int(input())
        myList1.append(ele)
if s2 < 0:
    print("Enter a valid size")
else:
    print("Input List2 : ")
    for i in range(0,s2):
        ele = int(input())
        myList2.append(ele)
# adding only the positive list elements to myOutput
for pos in myList1:
    if pos > 0:
        myOutput1.append(pos)
for pos in myList2:
    if pos > 0:
        myOutput2.append(pos)
# printing the positive numbers in the range
print("Output: ",end='')
print(*myOutput1,sep=',')
print("Output: ",myOutput2)