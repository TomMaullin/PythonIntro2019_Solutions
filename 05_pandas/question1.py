# Load in dataset
example_dataset = pd.read_csv('05_pandas/exercise_dataset.csv')

# Remove unwanted columns
example_dataset.drop(["age", "subject_ID"], axis=1)