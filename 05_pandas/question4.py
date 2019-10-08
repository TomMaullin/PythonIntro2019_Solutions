# Get quantile; assume quant is a decimal i.e. 0.05 for 5%
def myQuantile(inputArray, quant):
    
    # Sort the array
    sortedArray = np.sort(inputArray)
    
    # Work out index of quantile
    index = quant*len(inputArray)
    
    # We can get errors if they asked for 1\100%
    if index==len(inputArray):
        index = index-1
    
    return(sortedArray[np.int64(index)])
    
quantile(np.array([3,4,2,6,0,3]), 0.1)


# Apply to dataset
print('===============================')
print('My quantiles (0.05):')
print(example_dataset.select_dtypes(np.number).apply(myQuantile, quant=0.05))
print('Pandas quantiles (0.05):')
print(example_dataset.quantile(0.05))
print('===============================')
print('My quantiles (0.95):')
print(example_dataset.select_dtypes(np.number).apply(myQuantile, quant=0.95))
print('Pandas quantiles (0.95):')
print(example_dataset.quantile(0.95))

# Get the requested quantiles
upperHeartrate = example_dataset.heartrate.quantile(0.95)
lowerToeSize = example_dataset.size_of_left_toe.quantile(0.05)
print(upperHeartrate)
print(lowerToeSize)

# Get the requested data
example_dataset[(example_dataset['heartrate']>upperHeartrate) & 
                (example_dataset['size_of_left_toe']<lowerToeSize)]