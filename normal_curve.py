from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Creating the distributions
data = np.arange(1, 10, 0.1)
pdf = norm.pdf(data, loc=5.3, scale=1)

# Visualizing the distribution
sb.set_style('whitegrid')
sb.lineplot(x=data, y=pdf, color='black')  # Use x and y parameters to specify data
plt.xlabel('Heights')
plt.ylabel('Probability Density')
plt.show()
