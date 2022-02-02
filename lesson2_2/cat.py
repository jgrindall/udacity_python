"""A class that does someting."""

class Cat():
    """Holds a cat."""
    
    def __init__(self, name:str, age:int):
        """Make a cat.
        
        Arguments:
            name {str} -- the name of the cat
            age {int} -- the age of the cat in years
            
        """
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Say something.
        
        >>> kitty.speak()
        Spot says, purrrrrr.
        
        """
        print(f'{self.name} says, purrrrrr.')

        
if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'kitty': Cat('Spot', 3)})