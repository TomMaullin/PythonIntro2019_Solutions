# Make a new plot
plt.figure()

# Generate some Rayleigh random variables
r = stats.rayleigh.rvs(0,1,size=1000)

# Make a histogram
H = plt.hist(r,bins=30,density=True)

# Title the plot
plt.title("Normal Sample")

# Generate x values
x = np.linspace(0,4,1000)

# Add the pdf to the plot
plt.plot(x, stats.rayleigh.pdf(x), color='black', linewidth=2, label='normal')