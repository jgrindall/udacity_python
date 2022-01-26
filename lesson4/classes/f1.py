class Customer:
    def __init__(self, name1, name2, tier = ('free', 0)):
        self._name1 = name1
        self._name2 = name2
        self._tier = tier

    @property
    def name(self):
        return self._name1 + ' ' + self._name2
    
    def can_access(self, d):
        if self._tier[0] == 'free':
            return d["tier"] == 'free'
        return True
    
    def bill_for(self, months):
        if self._tier[0] == 'free':
            return 0
        return self._tier[1] * months
    
    @classmethod
    def premium(Cls, name1, name2):
        return Cls(name1, name2, ('premium', 10))
        
        
        
    


"""A few hints and clarifications:
The name can be a gettable property
The tier defaults to ('free', 0)"""


marco = Customer('Marco', 'Polo')  # Defaults to the free tier
print(marco.name)  # Marco Polo
print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
print(victoria.name)  # Alexandrina Victoria