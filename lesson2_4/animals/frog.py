from .animal import Animal

class Frog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self) -> None:
        """Make the frog noise"""
        print(f'{self.name} says, "rbbit rbbit"')
   