# Drop the rows with NaN for `size_of_left_toe` and `heartrate`
example_dataset = example_dataset.dropna(subset=['size_of_left_toe', 'heartrate'])