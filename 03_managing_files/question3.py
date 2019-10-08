# Loop through all files in directory
for fileName in os.listdir('.'):
    
    # Read in each file
    with open(fileName) as file:
        
        # Read random number
        randomNumber = float(file.read())
    
    # If the random number is less than zero delete the file
    if randomNumber<0:
        
        os.remove(fileName)
        