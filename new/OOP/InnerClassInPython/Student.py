# Understanding the concepts of inner class in pyhon
# First class student

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

# method to print the name and roll no of student
    def show(self):
        print(self.name, self.rollno)

# class containing addmission details of student
    class AdmissionDetails:  # contained students admission details
        def __init__(self, fall, major):
            self.fall = fall  # student admission year
            self.major = major  # student FSc major
            self.agg = 82.32  # Hardcoding the aggregate of student
        def show(self):
            print(self.fall, self.agg, self.major)

# class containing which laptop is used by student
    class Laptop:  # class containing student's laptop details
        def __init__(self):
            self.brand = "HP"
            self.processor = "i7"
            self.ram = 8
            self.ssd = 250

        def show(self):
            print(self.brand , self.processor, self.ssd, self.ram)