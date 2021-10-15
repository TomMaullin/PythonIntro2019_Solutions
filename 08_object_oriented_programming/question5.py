# -------------------------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------------------------

# Class for a quarternion
class Quaternion(object):
    
    # Simple init class
    def __init__(self,a,b,c,d):
        
        # Save each component
        self.__real = a
        self.__i = b
        self.__j = c
        self.__k = d
        
        # np array version
        self.__nparray = np.array([self.__real,self.__i,self.__j,self.__k])
        
    # Return a string representing the quarternion object
    def __str__(self):
        return(str(self.__real) + ' + ' + 
               str(self.__i) + 'i + ' + 
               str(self.__j) + 'j + ' + 
               str(self.__k) + 'k')
    
    # Return a string representing the quarternion object
    def __repr__(self):
        return('Quaternion')
    
    # Get the value of the quaternion
    @property
    def value(self):
        return(self.__nparray)
    
    
    # Get the conjugate of the quaternion
    @property
    def conjugate(self):
        return(Quaternion(self.__real,-self.__i,-self.__j,-self.__k))
    
    # Get the norm of the quaternion
    @property
    def norm(self):
        # Return result
        return(np.sqrt(self.__real**2 + self.__i**2 + self.__j**2 + self.__k**2))
    
    # Check if the two quarternions are equal
    def __eq__(self,q2):
        return(np.all(self.value==q2.value))
    
    # Check if the two quarternions are not equal
    def __ne__(self,q2):
        return(np.any(self.value!=q2.value))
    
    # Add q2 to self
    def __add__(self,q2):
        return(Quaternion(*(self.value+q2.value)))
    
    # Subtract q2 from self
    def __sub__(self,q2):
        return(Quaternion(*(self.value-q2.value)))
    
    # Multiply self by q1
    def __mul__(self,q2):
        
        # Unpack values
        a1, b1, c1, d1 = self.value
        a2, b2, c2, d2 = q2.value
        
        # Return result
        return Quaternion(a1*a2 - b1*b2 - c1*c2 - d1*d2,
                          a1*b2 + b1*a2 + c1*d2 - d1*c2,
                          a1*c2 - b1*d2 + c1*a2 + d1*b2,
                          a1*d2 + b1*c2 - c1*b2 + d1*a2)
        
    # Multiply self by q1 inversed
    def __truediv__(self, q2):
        
        # Get q2 values
        r, i, j, k = q2.value
        
        # Sum of squares
        ss = r**2 + i**2 + j**2 + k**2
        
        # Inverse q2 
        q2inv = Quaternion(r/ss,-i/ss,-j/ss,-k/ss)
        
        # Return result
        return(self*q2inv)

# -------------------------------------------------------------------------------------------
# Testing
# -------------------------------------------------------------------------------------------

import numpy as np
q1 = Quaternion(1,2,3,5)
q2 = Quaternion(8,1,2,1)

print('------------------------------')
print('q1:           ', q1)
print('q2:           ', q2)
print('------------------------------')
print('q1+q2:        ', q1+q2)
print('q1-q2:        ', q1-q2)
print('------------------------------')
print('q1*q2:        ', q1*q2)
print('q1/q2:        ', q1/q2)
print('------------------------------')
print('q1==q1:       ', q1==q1)
print('q1==q2:       ', q1==q2)
print('q1!=q1:       ', q1!=q1)
print('q1!=q2:       ', q1!=q2)
print('------------------------------')
print('q1.norm:      ', q1.norm)
print('q1.value:     ', q1.value)
print('q1.conjugate: ', q1.conjugate)