#The variable names `xyz` and `xyzsquared` are pointing to the same array. When we squared `xyzsquared` we also squared `xyz`.
# We could have avoided this by making `xyzsquared` a seperate copy of `xyz` using the `list` constructor like so:

xyzsquared = list(xyz)