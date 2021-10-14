# Here's a class representing an apple
class apple(object):
    
    # Initalize apple
    def __init__(self):
        pass
    
# Here's a class representing an orange
class orange(object):
    
    # Initialize orange
    def __init__(self):
        pass
    
# Here's a class representing a saxophone
class saxophone(object):
    
    # Initialize saxophone
    def __init__(self):
        pass
    
    
# Fruitbowl class
class fruitbowl(object):
    
    # Initialize fruit bowl
    def __init__(self, fruit = None):
        self.fruit = fruit
        
    # Add method
    def __add__(self, fruit):
        
        # Let's make a new bowl
        all_fruit = self.fruit
        
        # Check if the fruit is already there
        if all_fruit:
            if fruit in all_fruit:
                raise ValueError("That fruit is already in the fruitbowl!")
        
        # If it's fruit lets add it to a new bowl
        if type(fruit) in [apple, orange]:
            if not all_fruit:
                all_fruit = [fruit]
            else:
                all_fruit.append(fruit)
        else:
            
            raise ValueError("That's not a fruit! You can't put that in a fruitbowl!")
        
        # Return fruitbowl
        return(fruitbowl(all_fruit))
    
    # Subtraction function
    def __sub__(self,fruit):
        
        # Let's make a new bowl
        all_fruit = self.fruit
        
        # Check if the fruit is already there
        if all_fruit:
            if fruit in all_fruit:
                
                # Remove the fruit
                all_fruit = [f for f in all_fruit if f!= fruit]
                
            else:
                
                # Error
                raise ValueError("That fruit is not in this fruitbowl!")
                
        else:
            raise ValueError("There is no fruit in the fruitbowl!")
                
        return(fruitbowl(all_fruit))
        
            
    # Print the contents of the fruitbowl
    def contents(self):
        
        print('This fruitbowl contains: ')
        
        if self.fruit:
            for fruit in self.fruit:

                if type(fruit)==apple:
                    print(' - An apple')
                if type(fruit)==orange:
                    print(' - An orange')
        else:
            print('   Nothing!')
            
# ------------------------------------------------------------------------
# Testing the addition function
# ------------------------------------------------------------------------
# Make an apple and a fruitbowl
a = apple()
f = fruitbowl()

# Add an apple to the fruitbowl and check it's contents
f = f + a
f.contents()

# Add the same apple again.
f = f + a

# ------------------------------------------------------------------------
# Testing the subtraction function
# ------------------------------------------------------------------------

# Fruitbowl and apple
f = fruitbowl()
a = apple()

# Add an apple and see contents
f = f + a
f.contents()

# Subtract an apple and see contents
f = f - a
f.contents()

# Second apple test
a2 = apple()
f = f + a 
f = f - a2

