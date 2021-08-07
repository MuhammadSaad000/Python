MyDict = {
    "Name ": "Umer ",
    "Age  ": 23,
    "Roll No. ": "BSEF19M012",
    "Subjects ": ["COAL ", "PF", "OOP"]
}

print(MyDict)
print(MyDict.values())  # Print the values stored after colon in Dict

NewDict = MyDict.copy()  # copying a dictionary
print(NewDict)

print(len(MyDict))  # Printing no. of items present in dict

print(MyDict.keys())  # Shows which items are stored in list

print(MyDict.items())  # Get a list of the key:value pairs

# Changing contents of items in dictionary

# Dictionaries in Python  
MyDict["Name "] = "Saleem "  # changing a key of dictionary

# OR

MyDict.update({"Subjects ": ["CC ", "WW ", "DSA"]})

# Adding Items in lists

MyDict["Dropped "] = [1, 2, 3]  # Adding can also be done by Update Function above

# Deleting items from list
del NewDict["Subjects "]

print(MyDict.pop('Roll No. '))  # Will delete and print the entry from Dict
print(NewDict)
del NewDict  # Delete the whole dictionary

# Looping thriough dictionary
for x, y in MyDict.items():
    print(x, y)
