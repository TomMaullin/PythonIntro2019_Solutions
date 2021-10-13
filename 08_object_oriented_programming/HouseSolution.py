# ------------------------------------------------------------------------
# Check the House's methods
# ------------------------------------------------------------------------
object_looking_at = House

# Get the methods
object_methods = [method_name for method_name in dir(object_looking_at)
                  if callable(getattr(object_looking_at, method_name))]

# Print the methods
for object_method in object_methods:
    print(object_method)

# ------------------------------------------------------------------------
# Get the room list
# ------------------------------------------------------------------------
house.howToUseMethodByName('listRooms')
roomlist = house.listRooms()

# ------------------------------------------------------------------------
# Work out how to look for items
# ------------------------------------------------------------------------
house.howToUseMethodByName('isItemInRoom')

# ------------------------------------------------------------------------
# Look for valve
# ------------------------------------------------------------------------
for room in roomlist:
    house.isItemInRoom('Valve',room)

# ------------------------------------------------------------------------
# Look for dog
# ------------------------------------------------------------------------
house.isItemInRoom('dog','Kitchen')

# ------------------------------------------------------------------------
# Work out dog's name
# ------------------------------------------------------------------------
house.roomDescription('kennel')

# ------------------------------------------------------------------------
# Look for spike
# ------------------------------------------------------------------------
for room in roomlist:
    house.isItemInRoom('spike',room)

# ------------------------------------------------------------------------
# Look for kid
# ------------------------------------------------------------------------
for room in roomlist:
    house.isItemInRoom('kid',room)

# ------------------------------------------------------------------------
# Turn valve again
# ------------------------------------------------------------------------
house.isItemInRoom('Valve','Bedroom')

# ------------------------------------------------------------------------
# Describe chamber of death
# ------------------------------------------------------------------------
house.roomDescription("chamberofdeath")

# ------------------------------------------------------------------------
# Get book
# ------------------------------------------------------------------------
book = house.roomDescription("chamberofdeath")

# ------------------------------------------------------------------------
# Get book's methods
# ------------------------------------------------------------------------
# What is the object we're looking at
object_looking_at = type(book)

# Get the methods
object_methods = [method_name for method_name in dir(object_looking_at)
                  if callable(getattr(object_looking_at, method_name))]

# Print the methods
for object_method in object_methods:
    print(object_method)

# ------------------------------------------------------------------------
# Perform raindance
# ------------------------------------------------------------------------
book.performIncantation('raindance')

# ------------------------------------------------------------------------
# Activate sprinklers
# ------------------------------------------------------------------------
house.activateSprinklerSystem=True
house.turnOnSprinklers()