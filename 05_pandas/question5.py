# Obtain `mean_age_sex` and `mean_age_group`
mean_age_sex = example_dataset.groupby([pd.cut(example_dataset.age, bins=(9, 19, 29, 39, 49, 59)), 
                                        'sex']).mean()

mean_age_group = example_dataset.groupby([pd.cut(example_dataset.age, bins=(9, 19, 29, 39, 49, 59)), 
                                        'group']).mean()

# Obtain stacked table
stacked = pd.concat([mean_age_sex,mean_age_group])

# Reasons why you would not concatenate the tables in this way.
#  - sex and group are now merged, making the data harder to interpret
#  - If you wished to seperate `sex` and `group` into their original format it is now 
#    extremely difficult
#  - It will be much harder in future to see if there is any interaction between sex and
#    group