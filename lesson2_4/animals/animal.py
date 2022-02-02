from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def speak(self) -> None:
        """Make the frog noise"""
        print(f'{self.name} says, "rbbit rbbit"')
