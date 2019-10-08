# Don't worry if you don't understand the below yet,
# all you need know is x and y are random integers
import random
x = random.randint(0,3)
y = random.randint(0,3)

print(x, y)
try:
    z=x/y
except ZeroDivisionError as e:
    print('whoops divided by zero')

 if y==0:
 	print('whoops divided by zero')