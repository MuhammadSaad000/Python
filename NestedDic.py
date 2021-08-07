
# Nested Dictionaries
Students = {
    "Student1": {
        "Name": "Ali",
        "Age ": 21,
        "RollNo ": 11
    },

    "Student2": {
        "Name": "Raheel",
        "Age ": 21,
        "RollNo ": 1,
        "Blood Group ": "B+ve"
    },

    "Student3": {
        "Name": "Raza",
        "Age ": 21,
        "RollNo ": 4,
        "Blood Group ": "B+ve"
    }
}

print(Students.keys())
del Students["Student1"]    # Data of 1st student is deleted
print(Students.keys)
print(type(Students))

print("Data of Student2 : ", Students.get("Student2"))

for i, j in Students.items():
    print("Student No. ", i)
    print()
    for each in j:
        print(each, j[each])


print('Student deleted is : ',Students.popitem())