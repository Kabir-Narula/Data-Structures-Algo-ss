from abc import ABC, abstractmethod  # abc here means abstract base classes

class Vehicle(ABC):
  
    @abstractmethod
    def go(self):
        pass
  
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Car is moving")
    
    def stop(self):
        print("Car is stopped")

car = Car()

car.go()
car.stop()
