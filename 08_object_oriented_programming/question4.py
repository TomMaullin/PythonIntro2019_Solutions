# ---------------------------------------------------------------------------------------------------
# Some pros:
# ---------------------------------------------------------------------------------------------------
# - OOP allows you to organize your code and might make your code conceptually easier to understand
#   (emphasis on *might*).
# - OOP allows you finer control over what types of variables may be set and retreived (e.g. you can
#   ensure that a server serial number is an `int` property for example). Essentially it gives you a
#   standardised way of controlling what the user can save.
# - reduces code reproduction (only have to bug test one thing)
# - streamlined way of modelling between server differences and sims
# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
# Some cons
# ---------------------------------------------------------------------------------------------------
# - OOP can often unneccesarily overcomplicate code. 
# - OOP can often lead to more code maintainance in the long run. For example, if new servers are
#   continually being released and put into service, you may find yourself having to continually 
#   edit your classes (or even worse completely recreate your classes) to account for new unforseen 
#   features.
# - If you're using inheritance for OOP (which is very likely) it can sometimes become quite tricky
#   to keep track of which method is coming from where (e.g. `am I running the code from my class, 
#   or from some superclass of my class?`, see the answer to question 4 for a particularly nasty
#   example of this). This can make debugging a bit of a nightmare!
# ---------------------------------------------------------------------------------------------------