from abc import ABC, abstractmethod

# Define an abstract class
class Abstractdemo(ABC):
   @abstractmethod
   def car(self):
        pass  # Abstract method should not have an implementation

# Define a concrete subclass
class Demo(Abstractdemo):
    def car(self):
        print("PULSAR")

# Instantiate the concrete class and call the method
demo1 = Demo()
demo1.car()  # This will print "PULSAR"

# Attempting to instantiate the abstract class will raise an error
try:
    demo2 = Abstractdemo()
    demo2.car()
except TypeError as e:
    print(e)  # This will print an error message

