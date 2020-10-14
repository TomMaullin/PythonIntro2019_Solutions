# There are a lot of potentially good ways of going about this question.
# Below is one example. 

# --------------------------------------------------------------------------
# Use the Kolmogorov Smirnoff test to see if the distributions look normal.
# --------------------------------------------------------------------------
print(stats.kstest(sample1, 'norm'))
print(stats.kstest(sample2, 'norm'))
print(stats.kstest(sample3, 'norm'))
print(stats.kstest(sample4, 'norm'))

# When I ran this I found strong evidence that sample 1 was not normal.

# --------------------------------------------------------------------------
# Test the mean value of the remaining 3 functions to see if they have 0
# mean
# --------------------------------------------------------------------------
print(stats.ttest_1samp(sample2, popmean=0))
print(stats.ttest_1samp(sample3, popmean=0))
print(stats.ttest_1samp(sample4, popmean=0))

# When I ran this I found all 3 tested provided no evidence that the samples
# were drawn from a population with zero mean.

# -------------------------------------------------------------------------
#
# You could go further and test for the variance using chi^2 or F tests, 
# but these require normality assumptions which may or may not hold 
# (remember the first tests only provide evidence that a sample is not
# normal - not the other way around!).
#
# -------------------------------------------------------------------------
#
# As noted in the question, you have done multiple tests here and must 
# account for the multiple testing problem! A simple way to account for 
# this would be to use a Bonferoni correction which divides your alpha
# level by the number of tests you have done (in this case 7).
#
# -------------------------------------------------------------------------
#
# Also noted in the question was the risk of `p-hacking` or `data-dredging`.
# This is basically where you keep testing your data until you get the  
# result you want, regardless of whether the result is actually true. This
# is a big problem and you must not do it! In this question you can account
# for this by using multipe comparison corrections, or by generating new
# data for each test (which in real life corresponds to starting your 
# study from scratch and collecting new data!).
#
# -------------------------------------------------------------------------
