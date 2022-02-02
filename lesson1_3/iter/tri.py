""" 

The Tribonacci numbers are defined recursively, like the Fibonacci 
numbers, except that each subsequent number is the sum of the previous 
three. The first three Tribonacci numbers are 0, 0, 1. The next 
Tribonacci numbers in the sequence are 1, 2, 4, 7, 13, 24, 44, 81, ... 

Write a generator function generate_tribonacci_numbers that generates an 
infinite stream of Tribonacci numbers. It will look very similar to the 
generate_fibs function we saw previously. 

Then, write a function is_tribonacci that checks if a given number is a 
Tribonacci number. Be careful! You'll need to stop your search for a 
match if the Tribonacci number you're generating get too big. 
Specifically - the implementation return num in 
generate_tribonacci_numbers() will work fine when the number is a 
Tribonacci number, but will continue infinitely if not.

"""


def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    while True:
      oldC = c
      oldB = b
      c = a + b + c
      a = oldB
      b = oldC
      yield a
   
   
def is_tribonacci(num):
   """Return whether `num` is a Tribonacci number."""
   g = generate_tribonacci_numbers()
   while True:
      tri = next(g)
      if tri > num:
         return False
      elif tri == num:
         return True
   return False
   
   
   
   
   
print(is_tribonacci(4))
print(is_tribonacci(89))
print(is_tribonacci(90))

   