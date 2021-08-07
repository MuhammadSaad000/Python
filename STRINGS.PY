 #STRING SLICING IN PYTHON....
text = "Lahore is safest city in Pakistan"
print("safest" in text)     # Returns true if phrase exists

str_in = str(input("Enter the string "))
str_two = str(input("Enter the phrase to check in above string "))

if str_two in str_in:   # Above task can also be done using if condition
    print("Phrase is present ")
else:
    print("Phrase not present in the given string ")

# Similarly it can also be checked that phrase is not present using NOT IN


# We can cut a portion of string like we done in Lists
txt = "Hello World in Python"
print(txt[1:8])     # first index is included but not last index

print(txt[1:-4])        # -1 IS FIRST INDEX FROM LAST -2 2nd last and so on both indices are included in this

print(txt[:7])     # get characters from index(0 to 6 total = 7) 7 not included

print(txt[-8:-5])


# LISTS IN PYTHON.....
count = 0
num = [1, 9, 3, 41, 778, 90, 21, 13232, 231]
for i in num:
    count = count + 1
print("Total no of elements in a list is ", count)
