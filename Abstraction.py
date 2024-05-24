from abc import ABC, abstractmethod

class Abstractdemo(ABC):
   @abstractmethod
   def car(self):
        print("AUDI")
class Demo(Abstractdemo):
    def car(self):
        print("PULSAR")
demo1=Demo()
print(demo1.car())
demo2=Abstractdemo()
print(demo2.car())
