# 3a
# ----------------------------------------------------------------------------------------
# For the first part of this question, we are able to run subtraction and multiplication
# because we have inherited these methods from the `int` class (see where we define the
# class we wrote `def class inconsistInt(int):`, not `def class inconsistInt(object):`).
#
# It might not be desirable to inherit from the int class in this way as you could now use
# the methods from int to get values that are larger than n+p or less than 0. For example,
# try:
#
# print(b-a)
# print(b*a)
#
# Our original definition of inconsistent integers did not allow for this.
# ----------------------------------------------------------------------------------------
# You might argue `well yes, but why don't we just redefine these operations too?` and 
# you would have a point! The problem is, the `int` class has a lot of methods and it will
# be a lot of work, as well as potentially unnecessary code, to write over every single
# one!
# 
# On top of that, even if you did do this, there is nothing preventing someone behind
# the scenes in python one day changing the `int` class slighlty without you realizing, 
# and making all your hard work redundant (this happens more often than you'd think!)!
#
# Be very careful when choosing where and how to implement objects and classes!
# ----------------------------------------------------------------------------------------

# 3b
# ----------------------------------------------------------------------------------------
# The bug in this question is occuring inside the `__add__` function when the result is 
# being returned. The code in the question looks like this:
# ---------------------------------------------------------------------------------------- 

# Get result
if sval + aval <= n:
   result = sval + aval
else:
   result = inconsistInt(n + ((sval + aval -n)%p))

# ---------------------------------------------------------------------------------------- 
# But should look like this:
# ---------------------------------------------------------------------------------------- 

# Get result
if sval + aval <= n:
   result = inconsistInt(sval + aval)
else:
   result = inconsistInt(n + ((sval + aval -n)%p))

# ---------------------------------------------------------------------------------------- 
# The reason for this is as follows;
# ---------------------------------------------------------------------------------------- 
# Before we fixed the bug, when we ran "a+c+b" what was really happening `under the hood`
# was this:
# ---------------------------------------------------------------------------------------- 

(a.__add__(c)).__add__(b)

# ---------------------------------------------------------------------------------------- 
# a is an `inconsistInt`, so when we ran `a.__add__(c)` the method `__add__` was run 
# from the `inconsistInt` class and as (a+c>n) the `else` statement in the code above was
# called.
#
# As the `else` statement was called the result of this was another inconsistInt, say
# d = a.__add__(c). When the second __add__ in the above, it was as though we had run
# d.__add__(b). As d is an inconsistInt, we again called the method `__add__` from the 
#`inconsistInt` class 
#
# As a result a+c+b was running correctly!
#
# However, when we ran `a+b+c` what we were really doing was this:
# ---------------------------------------------------------------------------------------- 

(a.__add__(b)).__add__(c)

# ---------------------------------------------------------------------------------------- 
# As before, a is an `inconsistInt`, so when we ran `a.__add__(b)` the method `__add__`
# was run from the `inconsistInt` class. However, as (a+b<=n) the `if` statement in the 
# code above was called. This returned an int, not an inconsistInt! 
#
# In other words, if we had set f = a.__add__(b), then f would have been an `int` not an
# `inconsistInt`. This meant that when we ran the second __add__ function, what we were
# really doing was:
#
# f.__add__(c)
#
# but as f was an int, we were calling `__add__` from the normal int class, not from the
# inconistInt class! This meant that the function just added the values of f and c in the
# normal ways, i.e. without doing all the modulo stuff!
#
# That caused the error!!
# ---------------------------------------------------------------------------------------- 
# Very well done to anyone who spotted this! It's not an easy bug to spot!
# ---------------------------------------------------------------------------------------- 