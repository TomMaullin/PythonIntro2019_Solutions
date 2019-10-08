# The time function can be imported like so
from time import time

# We can see it's documentation here
help(time)

# It can be used to time code in seconds e.g.
t1 = time()
for i in range(100):
  print(i)
t2 = time()

print("Printing the numbers 1-100 took ", t2-t1, " seconds.")