from time import process_time
  
t0 = process_time() 
n0 = 9 in map(lambda x: x ** 2, range(1000000))
t1 = process_time()
   
print(n0)
print("Elapsed time:", t0, t1, t1 - t0)

t0 = process_time() 
n1 = 9 in [x ** 2 for x in range(1000000)]
t1 = process_time()

print(n1)
print("Elapsed time:", t0, t1, t1 - t0)

a = [x**5 for x in range(0, 10)]
print(a)