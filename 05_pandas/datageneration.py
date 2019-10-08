# The below code was used to generate the example dataset for notebook 5.

import random
import string
n = 5000

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

filelist = []
for sub in range(n):
    
    filelist = filelist + ['file_' + randomString(10) + '.txt']

example_dataset = pd.DataFrame.from_dict({
                    'size_of_left_toe': np.random.rand(n),
                    'subject_ID': np.arange(1200,1200+n),
                    'age': np.random.randint(10, 60, size=n),
                    'group': random.choices(["A", "B", "C", "D", "E"],k=n),
                    'heartrate': np.random.uniform(low=60,high=100,size=n),
                    'favourite_animal': random.choices(["hedgehog", "cat", "dog", "zebra", "bat", "shrimp", "Fossa", "Hoatzin", "Lammergeier", "Predatory Hawaiian Caterpillar", "Giant Otter", "Atretochoana", "Chinese Giant Salamander", "Clawed Frog", "Eastern Long-necked turtle", "Mexican Mole Lizard", "Spike nosed tree frog", "Kakapo", "Long-wattled umbrella bird", "Shark", "Goldfish", "Hickory Horned devil","giraffe","rhino", "turnip"], weights = [8, 10, 10,6, 4, 4, 3, 1, 1, 1, 2, 2, 1, 1, 2, 3, 1, 2, 1, 10, 10,1,5,4,0.5],k=n),
                    'sex': random.choices(["M", "F"],k=n),
                    'additional_info': filelist
})
print(example_dataset.shape)

# Add in some missing data
rows = np.random.randint(0,n,size=n//10)
cols = np.random.randint(0,7,size=n//10)
for i in range(n//10):
    example_dataset.iloc[rows[i],cols[i]]= np.nan

example_dataset.to_csv('05_pandas/exercise_dataset.csv')
example_dataset