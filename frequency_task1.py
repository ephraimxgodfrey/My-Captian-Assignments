# program to print the letters in a string in the decreasing order of their frequency:

# creating a user defined function most_frequent
def most_frequent ():
# getting input from the user 
    word = str(input("Enter the string : ")).lower()
# empty dictionary which will later store the individual letters and their frequency
    freq = {}
# calculating the frequency of each letter in the string
    for i in range(len(word)):
        count = 0
        for letter in word:
            if word[i] == letter:
                count = count + 1
# adding the letters and their corresponding frequency to the dictionary freq
        freq[word[i]] = count
# sorting the dictionary based on the value in the descending order
    sort_orders = sorted(freq.items(), key=lambda x: x[1], reverse = True)
# printing the output in the specified format
    for i in sort_orders:
	    print(i[0],"=", i[1])

# calling the function 
most_frequent()