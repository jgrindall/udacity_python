from .animal import Animal
       
class Cat(Animal):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        """Create a new cat"""
        super().__init__(name, age)
        
        self.isIndoor = isIndoor

    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')
        
