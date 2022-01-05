# program to accept a filename and print its extension

# accepting the filename from the user
filename = str(input("Input the filename: "))
# spliting the root and the extension
split = filename.split(".")
# storing the extension seperately
extension = split[1]
# printing the extension of the filename
print("The extension of the file is: " + extension)