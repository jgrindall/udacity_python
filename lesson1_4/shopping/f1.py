class User:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._reviews = []
    @property
    def id(self):
        return self._id

    def sell_product(self, name, descr, price):
        return Product(name, descr, self, price, True)
    def buy_product(self, p):
        p.available = False
        pass
    def write_review(self, descr, p):
        r = Review(self, descr, p)
        self._reviews.append(r)
        p.add_review(r)
        return r
        
    def __str__(self):
        return "User " + self._name + " (" + self._id + ")"
        
    @property
    def reviews(self):
        return self._reviews
    

class Product:
    def __init__(self, name, descr, seller, price, available):
        self._reviews = []
        self._descr = descr
        self._name = name
        self._price = price
        self._available = available
        
    @property
    def name(self):
        return self._name
    
    @property
    def descr(self):
        return self._descr
        
    @property
    def available(self):
        return self._available
        
    @available.setter
    def available(self, a):
        self._available = a
        
    def add_review(self, r):
        self._reviews.append(r)
        
    @property
    def reviews(self):
        return self._reviews
    
    def __str__(self):
        return "p"
        
        
        
class Review:
    def __init__(self, user, descr, product):
        self._user = []
        self._descr = descr
        self._product = product
        
    @property
    def name(self):
        return self._name
    
    @property
    def descr(self):
        return self._descr
        
    def __str__(self):
        return "r"

#A User will have an id and a name, and be able to sell_product, buy_product, and write_review.
#A Product will contain a name, a description, a seller, a collection of reviews, a price, and an availability.
#A Review will contain a description, a user (who wrote the review), and a product (for which the review is written)
#Each of these classes should be nicely printable.

#By the time you're done, the following lines of code should be valid:

brianna = User(1, 'Brianna')
mary = User(2, 'Mary')


keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)
print(keyboard.available)  # => False

review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True
