# Use value counts to see the animals and their frequency
example_dataset['favourite_animal'].value_counts()

# The only non-animal in this list is a turnip.
# Remove all rows with turnip like so.
example_dataset = example_dataset[example_dataset['favourite_animal']!='turnip']

# Quick check
example_dataset['favourite_animal'].value_counts()