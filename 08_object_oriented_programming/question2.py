# Class for a paraconsistent boolean
class paraconsistentBoolean(object):
    
    # Initialize class
    def __init__(self, value):
        
        if type(value)==str:
            value = value.lower()
        
        # Check if value is true and true only
        if value==True or value=='true':
            
            # Save result
            self.isTrue = True
            self.isFalse = False
        
        # Check if value is false and false only
        elif value==False or value=='false':
            
            # Save result
            self.isTrue = False
            self.isFalse = True
        
        # Check if its both true and false
        elif value=='both':
            
            # Save result
            self.isTrue = True
            self.isFalse = True
            
        # Otherwise return an error
        else:
            
            raise ValueError("Invalid value for a paraconsistent boolean!")
            
    # Get the value of the paraconsistent boolean
    def value(self):
        
        # If true and true only
        if self.isTrue and not self.isFalse:
            return('True')
        
        # If false and false only
        if not self.isTrue and self.isFalse:
            return('False')
        
        # If both
        if self.isTrue and self.isFalse:
            return('Both')
       
    # Define `&`
    def __and__(self, secondBool):
        
        # New result of `and` operation
        resultIsFalse = False
        resultIsTrue = False
        
        # If both of them are one of true or both, the result is true (or both)
        if self.isTrue and secondBool.isTrue:
            
            # Save result
            resultIsTrue = True
            
        # If one is false (or both) then the result is false (or both)
        if self.isFalse or secondBool.isFalse:
            
            # Save result
            resultIsFalse = True
        
        # Get result
        if resultIsFalse and not resultIsTrue:
            
            # initalize result
            r = paraconsistentBoolean('False')
            
        elif not resultIsFalse and resultIsTrue:
            # initalize result
            r = paraconsistentBoolean('True')
            
        elif resultIsFalse and resultIsTrue:
            
            # initalize result
            r = paraconsistentBoolean('Both')
            
        else:
            
            raise ValueError('Somethings gone wrong here!')
            
        return(r)
       
    # Define not/~
    def __invert__(self):
        
        # If false, return true
        if not self.isTrue and self.isFalse:
            return(paraconsistentBoolean('True'))
        
        # If true, return false
        elif not self.isFalse and self.isTrue:
            return(paraconsistentBoolean('False'))
        
        # Else return both
        elif self.isFalse and self.isTrue:
            return(paraconsistentBoolean('Both'))
        
       
    # Define `|`
    def __or__(self, secondBool):
        
        # Luckily, De Morgans law holds
        return(~((~self) & (~secondBool)))
            
# -----------------------------------------------------------------------------------------
# Test it out!
# -----------------------------------------------------------------------------------------

# Make some paraconsistent booleans
a = paraconsistentBoolean(True)
b = paraconsistentBoolean(False)
c = paraconsistentBoolean('Both')

# Run and for all possible combinations
d = a & b
e = b & c
f = c & a
g = a & a
h = b & b
i = c & c

# Run not for all possible combinations
j = ~a
k = ~b
l = ~c

# Run or for all possible combinations
m = a | b
n = b | c
o = c | a
p = a | a
q = b | b
r = c | c

# Print the values of each
print('a: ', a.value())
print('b: ', b.value())
print('c: ', c.value())
print('----------------------')
print('d: ', d.value())
print('e: ', e.value())
print('f: ', f.value())
print('g: ', g.value())
print('h: ', h.value())
print('i: ', i.value())
print('----------------------')

# Try out not function
print('j: ', j.value())
print('k: ', k.value())
print('l: ', l.value())

# Try out or function
print('----------------------')
print('m: ', m.value())
print('n: ', n.value())
print('o: ', o.value())
print('p: ', p.value())
print('q: ', q.value())
print('r: ', r.value())
print('----------------------')