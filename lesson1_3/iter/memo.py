import random
import itertools
import functools

def memoize(function):
   function._cache = dict()
   @functools.wraps(function)
   def wrapper(*args, **kwargs):
      key0 = '-'.join(str(x) for x in args)
      key1 = '-'.join(str(x) + '=' + str(y) for x, y in kwargs.items())
      key = key0 + key1
      #print(key)
      if key in function._cache:
         return function._cache[key]
      else:
         val = function(*args, **kwargs)
         function._cache[key] = val
         return val
   return wrapper


@memoize
def fib(n):
   if n < 2:
      return n
   return fib(n - 1) + fib(n - 2)




print(fib(10))
print(fib(25))
print(fib(50))
print(fib(100))