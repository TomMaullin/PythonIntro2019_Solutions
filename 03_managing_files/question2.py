# Import the random package
import random

# Use the gauss function to obtain a random number
randomNo = random.gauss(0, 1) # Random ~N(0,1) variable
print(randomNo)

# Loop through numbers one to twenty
for i in range(20):
    
    # New file number
    fileNo = str(i+1)
    
    # New file name
    fileName = 'test'+fileNo+'.txt'
    
    # Write a random number to the file
    with open(fileName, 'w') as file:
        file.write(str(random.gauss(0, 1)))