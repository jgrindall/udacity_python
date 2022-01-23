import random
import itertools

def random_list(size, start=0, stop=10):
   return list(random.randrange(start, stop) for _ in range(size))


"""Generate an infinite stream of successively larger random lists."""

def generate_cases():
   len = 0
   while True:
      len += 1
      yield random_list(len)



for case in generate_cases():
   if len(case) > 10:
      break
   print(case)
   
   
   
def generate_cases_another_alternative():
   return map(random_list, itertools.count())
   
   

for case in generate_cases_another_alternative():
   if len(case) > 10:
      break
   print(case)