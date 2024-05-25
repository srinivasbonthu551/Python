class Student:
    def __init__(self, name, rollno, age):
        self.name = name        # Public instance variable
        self._rollno = rollno   # Protected instance variable
        self.__age = age        # Private instance variable
    
    def display(self):
        print(f"HI myself {self.name} and age is {self.__age} from student class")

class Branch(Student):
    pass

# Creating an instance of Student
s1 = Student("Rahul", 22, 19)

# Accessing and printing the public instance variable
print(s1.name)  # Expected output: Rahul

# Accessing and printing the protected instance variable
print(s1._rollno)  # Expected output: 22

# Accessing and printing the private instance variable using name mangling
print(s1._Student__age)  # Expected output: 19

# Attempting to access the private instance variable directly (will raise an AttributeError if uncommented)
# print(s1.__age)

# Displaying information using the display method
s1.display()  # Expected output: HI myself Rahul and age is 19 from student class

# Creating an instance of Branch (inherited from Student)
b1 = Branch("Nisha", 23, 20)

# Accessing and printing the public instance variable from the Branch instance
print(b1.name)  # Expected output: Nisha

# Accessing and printing the protected instance variable from the Branch instance
print(b1._rollno)  # Expected output: 23

# Accessing and printing the private instance variable from the Branch instance using name mangling
print(b1._Student__age)  # Expected output: 20

# Displaying information using the display method from the Branch instance
b1.display()  # Expected output: HI myself Nisha and age is 20 from student class


